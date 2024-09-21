import unittest
from unittest.mock import patch, MagicMock
from src.openai_interface import generate_completion, get_embedding

class TestOpenAIInterface(unittest.TestCase):

    @patch('src.openai_interface.openai.ChatCompletion.create')
    def test_generate_completion(self, mock_create):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Test completion"
        mock_create.return_value = mock_response

        result = generate_completion("Test prompt")
        self.assertEqual(result, "Test completion")
        mock_create.assert_called_once()

    @patch('src.openai_interface.openai.Embedding.create')
    def test_get_embedding(self, mock_create):
        # Mock the API response
        mock_response = {'data': [{'embedding': [0.1, 0.2, 0.3]}]}
        mock_create.return_value = mock_response

        result = get_embedding("Test text")
        self.assertEqual(result, {'embedding': [0.1, 0.2, 0.3]})
        mock_create.assert_called_once()

if __name__ == '__main__':
    unittest.main()