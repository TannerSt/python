import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plot

from time import sleep
from PIL import ImageGrab


def screenshot():
	ss_region = (1000, 375, 1600, 650)
	ss_img = ImageGrab.grab(ss_region)
	ss_img.save(r"C:\Users\tsain\OneDrive\Pictures\Screenshots\tmp.png")


sleep(10)	#pause to get app open manually for now
screenshot()


image_1_path = r"C:\Users\tsain\OneDrive\Pictures\Screenshots\tmp.png"

def recognize_text(img_path):

	reader = easyocr.Reader(["en"])					#creates a list
	return reader.readtext((img_path), detail=0)	#specifies only text output without coordinates or confidence

result = recognize_text(image_1_path)





search_item = "20%"									#too specific of a match
found = False

for index, item in enumerate(result):				#searches result list for search item
	if item == search_item:
		found = True
		print(search_item)
		break

	#if not found:




#print(result)




img_1 = cv2.imread(image_1_path)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
plot.imshow(img_1)

def overlay_ocr_text(img_path, save_name):
    #loads an image, recognizes text, and overlays the text on the image
    
    # loads image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    dpi = 80
    fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
    plt.figure()
    f, axarr = plt.subplots(1,2, figsize=(fig_width, fig_height)) 
    axarr[0].imshow(img)

