
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def clean_text(text):
    """Clean and normalize resume text."""

    # Convert text into lowercase
    text = text.lower()

    # Replace unnecessary special characters
    # Preserve +, # and . for skills like C++, C#, .NET
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()



def tokenize_text(text):
    """Split text into meaningful words and technical terms."""

    words = re.findall(
        r"c\+\+|c#|\.net|[a-z0-9]+(?:[.-][a-z0-9]+)*",
        text
    )

    return words



def remove_stopwords(words):
    """Remove common English words."""

    filtered_words = [
        word for word in words
        if word not in ENGLISH_STOP_WORDS
    ]

    return filtered_words


def preprocess_resume(text):
    """Complete resume text preprocessing."""

    cleaned_text = clean_text(text)

    tokens = tokenize_text(cleaned_text)

    filtered_tokens = remove_stopwords(tokens)

    return {
        "cleaned_text": cleaned_text,
        "tokens": tokens,
        "filtered_tokens": filtered_tokens
    }
