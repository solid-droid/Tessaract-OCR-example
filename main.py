import pytesseract
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cv2_image = cv2.imread('image.PNG')
stripped_image = Image.fromarray(cv2_image)

text = pytesseract.image_to_string(stripped_image)

print(text)