import pytesseract
from PIL import Image

image_path = input("input path: ")
bahasa = 'eng'
image = Image.open(image_path)
result = pytesseract.image_to_string(image, lang=bahasa)
print("hasil: ", result)
 
