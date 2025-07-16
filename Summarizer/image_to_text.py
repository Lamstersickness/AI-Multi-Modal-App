import pytesseract
from PIL import Image
import os

# Add this path configuration (modify if your path is different)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        extracted_text = pytesseract.image_to_string(image)
        return extracted_text if extracted_text.strip() else "No text could be extracted from the image."
    except Exception as e:
        return f"Error extracting text: {str(e)}"