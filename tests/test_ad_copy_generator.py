import unittest
from unittest.mock import patch, MagicMock
from src.ad_copy_generator import AdCopyGenerator

class TestAdCopyGenerator(unittest.TestCase):

    def setUp(self):
        self.api_key = "test_api_key"
        self.generator = AdCopyGenerator(self.api_key)

    @patch('src.ad_copy_generator.generate_completion')
    def test_generate_ad_copy(self, mock_generate_completion):
        # Mock the generate_completion function
        mock_generate_completion.return_value = "Test ad copy 1\n\nTest ad copy 2"

        # Test parameters
        product = "Test Product"
        target_audience = "Test Audience"
        tone = "professional"
        length = 20

        # Generate ad copy
        result = self.generator.generate_ad_copy(product, target_audience, tone, length)

        # Check if the result is as expected
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "Test ad copy 1")
        self.assertEqual(result[1], "Test ad copy 2")

        # Check if generate_completion was called with the correct prompt
        expected_prompt = f"Generate an ad copy for Test Product targeting Test Audience. The tone should be professional and the length should be approximately 20 words."
        mock_generate_completion.assert_called_once_with(expected_prompt)

    @patch('src.ad_copy_generator.generate_completion')
    def test_analyze_ad_performance(self, mock_generate_completion):
        # Mock the generate_completion function
        mock_generate_completion.return_value = "Test performance analysis"

        # Test parameters
        ad_copy = "This is a test ad copy"
        metrics = {"click_through_rate": 0.05, "conversion_rate": 0.02}

        # Analyze ad performance
        result = self.generator.analyze_ad_performance(ad_copy, metrics)

        # Check if the result is as expected
        self.assertEqual(result, "Test performance analysis")

        # Check if generate_completion was called with the correct prompt
        expected_prompt = "Analyze the performance of the following ad copy:\n\nThis is a test ad copy\n\nMetrics:\n- click_through_rate: 0.05\n- conversion_rate: 0.02\n\nProvide insights and suggestions for improvement."
        mock_generate_completion.assert_called_once_with(expected_prompt)

if __name__ == '__main__':
    unittest.main()