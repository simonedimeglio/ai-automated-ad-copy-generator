import openai
from typing import Dict, Any

def generate_completion(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150) -> str:
    """
    Generate a completion using the OpenAI API.

    Args:
        prompt (str): The input prompt for the completion.
        model (str): The OpenAI model to use (default: "gpt-3.5-turbo").
        max_tokens (int): The maximum number of tokens in the response (default: 150).

    Returns:
        str: The generated completion text.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in generating completion: {str(e)}")
        return ""

def get_embedding(text: str, model: str = "text-embedding-ada-002") -> Dict[str, Any]:
    """
    Get the embedding for a given text using the OpenAI API.

    Args:
        text (str): The input text to embed.
        model (str): The OpenAI model to use for embedding (default: "text-embedding-ada-002").

    Returns:
        Dict[str, Any]: A dictionary containing the embedding and related information.
    """
    try:
        response = openai.Embedding.create(
            input=text,
            model=model
        )
        return response['data'][0]
    except Exception as e:
        print(f"Error in getting embedding: {str(e)}")
        return {}