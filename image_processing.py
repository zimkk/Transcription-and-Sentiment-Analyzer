from PIL import Image
import pytesseract
import nltk
nltk.download('punkt')

def convert_image_to_text(image_path):
    """
    Convert image to text using Tesseract OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text formatted into sentences.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        # Sentence segmentation and punctuation cleanup
        sentences = nltk.sent_tokenize(text)
        formatted_text = ". ".join(sentences)
        if formatted_text and formatted_text[-1] != ".":
            formatted_text += "."

        return formatted_text
    except Exception as e:
        print("Error:", e)
        return ""

