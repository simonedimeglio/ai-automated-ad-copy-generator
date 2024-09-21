from src.huggingface_interface import generate_text
from src.utils import sanitize_input

class AdCopyGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_ad_copy(self, product: str, target_audience: str, tone: str, length: int) -> list:
        product = sanitize_input(product)
        target_audience = sanitize_input(target_audience)
        tone = sanitize_input(tone)

        prompt = f"Write a {tone} ad copy of about {length} words for an {product}. Target audience: {target_audience}. Focus on eco-friendly benefits. The ad should be concise, engaging, and persuasive.\n\nAd Copy:"

        response = generate_text(prompt, self.api_key, max_length=length*4)
        
        # Post-process the response
        sentences = response.split('.')
        ad_copy = ''
        for sentence in sentences:
            if len(ad_copy.split()) + len(sentence.split()) <= length:
                ad_copy += sentence.strip() + '. '
            else:
                break
        
        return [ad_copy.strip()]

    def analyze_ad_performance(self, ad_copy: str, metrics: dict) -> str:
        prompt = f"""Analyze the performance of this ad copy: '{ad_copy}'
        
        Metrics:
        - Click-through rate: {metrics['click_through_rate']}
        - Conversion rate: {metrics['conversion_rate']}
        - Bounce rate: {metrics['bounce_rate']}
        
        Provide a brief analysis of the ad's performance based on these metrics. Suggest two specific improvements to boost its effectiveness.
        
        Analysis:"""

        analysis = generate_text(prompt, self.api_key, max_length=200)
        
        # Ensure we're not just repeating the prompt
        if "Provide a brief analysis" in analysis:
            analysis = analysis.split("Provide a brief analysis")[0].strip()
        
        return analysis