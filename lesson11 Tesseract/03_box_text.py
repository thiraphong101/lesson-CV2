import cv2
import pytesseract
from pytesseract import Output
img = cv2.imread('box_text.jpg')


# Get bounding box estimates
boxes = pytesseract.image_to_boxes(img) 
# boxes around text
h, w, c = img.shape
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
print(boxes)

# dictionary key
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())


# Simple image to string
text = pytesseract.image_to_string(img,lang="eng")
print(text)
cv2.imshow('img', img)
cv2.waitKey(0)