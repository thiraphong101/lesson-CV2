import cv2 
import pytesseract
print(pytesseract.__version__)
img = cv2.imread('book_page.jpg')#'sample2.png'
# Adding custom options
custom_config = r'--oem 3 --psm 6'
# Simple image to string
print(pytesseract.image_to_string(img, config=custom_config ,lang="eng"))
# Get bounding box estimates
print(pytesseract.image_to_boxes(img))
# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(img))
"""
อาร์กิวเมนต์ --psm มี 14 โหมด
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
 11    Sparse text. Find as much text as possible in
 no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
bypassing hacks that are Tesseract-specific.
"""