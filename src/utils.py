import re
from typing import List

def sanitize_input(text: str) -> str:
    """
    Sanitize the input text by removing any potentially harmful characters.

    Args:
        text (str): The input text to sanitize.

    Returns:
        str: The sanitized text.
    """
    # Remove any non-alphanumeric characters except spaces and common punctuation
    sanitized = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)
    return sanitized.strip()

def tokenize(text: str) -> List[str]:
    """
    Tokenize the input text into words.

    Args:
        text (str): The input text to tokenize.

    Returns:
        List[str]: A list of tokens (words).
    """
    # Simple tokenization by splitting on whitespace
    return text.split()

def calculate_word_count(text: str) -> int:
    """
    Calculate the word count of the given text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of words in the text.
    """
    return len(tokenize(text))

def truncate_text(text: str, max_words: int) -> str:
    """
    Truncate the text to the specified maximum number of words.

    Args:
        text (str): The input text to truncate.
        max_words (int): The maximum number of words to keep.

    Returns:
        str: The truncated text.
    """
    words = tokenize(text)
    if len(words) <= max_words:
        return text
    return ' '.join(words[:max_words]) + '...'