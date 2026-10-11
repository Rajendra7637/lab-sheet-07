"""Small text-cleaning helper shared by the main script and predict.py."""
import re

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def clean_text(text):
    """Lowercase the text, keep only letters, and remove stop words and tiny words.

    Example: "The company LAUNCHED 3 new phones!" -> "company launched new phones"
    """
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", " ", text)          # remove digits and punctuation
    words = [word for word in text.split() if len(word) > 2 and word not in ENGLISH_STOP_WORDS]
    return " ".join(words)
