import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')

def scrape_text_from_website(url):
    """
    Scrape text content from a website and format into sentences.

    Args:
        url (str): URL of the website.

    Returns:
        str: Extracted text formatted into sentences.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get text from paragraphs and other common text-containing elements
        text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'blockquote'])  # Add more elements if needed
        text = '\n'.join([elem.get_text() for elem in text_elements])

        # Sentence segmentation and punctuation cleanup
        sentences = nltk.sent_tokenize(text)
        formatted_text = ". ".join(sentences)
        if formatted_text and formatted_text[-1] != ".":
            formatted_text += "."

        return formatted_text
    except Exception as e:
        print("Error:", e)
        return ""


