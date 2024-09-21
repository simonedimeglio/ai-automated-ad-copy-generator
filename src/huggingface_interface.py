import requests
import json
import logging
import time
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://api-inference.huggingface.co/models/gpt2-xl"

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=60))
def query(payload, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    logger.info(f"Sending request to {API_URL}")
    response = requests.post(API_URL, headers=headers, json=payload)
    logger.info(f"Received response with status code: {response.status_code}")
    if response.status_code == 503:
        logger.warning("Model is loading. Retrying...")
        time.sleep(5)  # Wait for 5 seconds before retrying
        raise Exception("Model is loading")
    if response.status_code != 200:
        logger.error(f"Error response: {response.text}")
        raise Exception(f"API request failed with status code {response.status_code}")
    return json.loads(response.content.decode("utf-8"))

def generate_text(prompt, api_key, max_length=150):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "num_return_sequences": 1,
            "do_sample": True,
            "temperature": 0.9,  # Increased temperature for more creativity
            "top_k": 50,
            "top_p": 0.95
        }
    }
    try:
        response = query(payload, api_key)
        logger.info(f"API Response: {response}")
        if isinstance(response, list) and len(response) > 0:
            generated_text = response[0].get("generated_text", "")
            # Remove the original prompt from the generated text
            return generated_text[len(prompt):].strip()
        else:
            logger.error(f"Unexpected response format: {response}")
            return "Errore: Formato di risposta non valido."
    except Exception as e:
        logger.error(f"Error generating text: {str(e)}")
        return f"Errore: {str(e)}"