import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ad_copy_generator import AdCopyGenerator
from config import HUGGINGFACE_API_KEY

def main():
    # Initialize the AdCopyGenerator
    generator = AdCopyGenerator(HUGGINGFACE_API_KEY)

    # Example parameters
    product = "Eco-friendly reusable coffee cup"
    target_audience = "environmentally conscious millennials"
    tone = "inspiring and informative"
    length = 50

    print(f"Generating ad copy for '{product}'...")
    
    try:
        # Generate ad copies
        ad_copies = generator.generate_ad_copy(product, target_audience, tone, length)

        # Print the generated ad copies
        if ad_copies:
            for i, copy in enumerate(ad_copies, 1):
                print(f"\nAd Copy Variant {i}:")
                print(copy)
        else:
            print("No ad copies were generated.")
            return

        # Example performance metrics
        metrics = {
            "click_through_rate": 0.04,
            "conversion_rate": 0.02,
            "bounce_rate": 0.55
        }

        # Analyze the performance of the first ad copy
        if ad_copies[0] != "Errore: Impossibile generare il testo.":
            print("\nAnalyzing performance of the ad copy...")
            analysis = generator.analyze_ad_performance(ad_copies[0], metrics)
            print("\nPerformance Analysis:")
            print(analysis)
        else:
            print("Cannot perform analysis: No valid ad copy was generated.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your Hugging Face API key, quota, and internet connection.")

if __name__ == "__main__":
    main()