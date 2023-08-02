import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plot

image_1_path = r"C:\Users\tsain\OneDrive\Pictures\images_for_text\test.png"

def recognize_text(img_path):

	reader = easyocr.Reader(["en"])
	return reader.readtext(img_path)

result = recognize_text(image_1_path)

result

print(result)

img_1 = cv2.imread(image_1_path)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
plot.imshow(img_1)



def overlay_ocr_text(img_path, save_name):
    '''loads an image, recognizes text, and overlays the text on the image.'''
    
    # loads image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    dpi = 80
    fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
    plt.figure()
    f, axarr = plt.subplots(1,2, figsize=(fig_width, fig_height)) 
    axarr[0].imshow(img)