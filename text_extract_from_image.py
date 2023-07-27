import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plot

image_1_path = "C:\Users\tsain\OneDrive\Pictures\images_for_text\test.png"

def recognize_text(img_path):

	reader = easyocry.Reader(["en"])
	return reder.redtext(img_path)

result = recognize_text(image_1_path)
