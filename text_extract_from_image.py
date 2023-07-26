from PIL import Image
from pytesseract import pytesseract

image = Image.open("test.png")
image = image.resize((400,200))
image.save("sample.png")

path_to_tesseract = r"C:\Users\tsain\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\pytesseract"
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(image)
#print the text line by line
print(text[:-1])