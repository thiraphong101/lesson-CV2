import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('digits-task.jpg')
# Output with outputbase digits
hImg, wImg,_ = img.shape
custom_config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=custom_config)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
cv2.imshow('img', img)
cv2.waitKey(0)

# Output with a whitelist of characters (here, we have used all the lowercase characters from a to z only)
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))
cv2.imshow('img', img)
cv2.waitKey(0)

# Output without the blacklisted characters (here, we have removed all digits)
custom_config = r'-c tessedit_char_blacklist=0123456789 --psm 6' 
pytesseract.image_to_string(img, config=custom_config)
cv2.imshow('img', img)
cv2.waitKey(0)

# Output with only english language specified
custom_config = r'-l eng --oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))

# Output with all languages specified
custom_config = r'-l grc+tha+eng --oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))
cv2.imshow('img', img)
cv2.waitKey(0)

"""
Page segmentation modes
There are several ways a page of text can be analysed. The tesseract api provides several page segmentation modes if you want to run OCR on only a small region or in different orientations, etc.

Here's a list of the supported page segmentation modes by tesseract -

0    Orientation and script detection (OSD) only.
1    Automatic page segmentation with OSD.
2    Automatic page segmentation, but no OSD, or OCR.
3    Fully automatic page segmentation, but no OSD. (Default)
4    Assume a single column of text of variable sizes.
5    Assume a single uniform block of vertically aligned text.
6    Assume a single uniform block of text.
7    Treat the image as a single text line.
8    Treat the image as a single word.
9    Treat the image as a single word in a circle.
10    Treat the image as a single character.
11    Sparse text. Find as much text as possible in no particular order.
12    Sparse text with OSD.
13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
"""