from PIL import Image
import pytesseract
import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
    ROIimg = frame[200:300,100:400]
    cv2.rectangle(frame,(100,300),(400,200),(0,255,0),5)
    hsv = cv2.cvtColor(ROIimg, cv2.COLOR_BGR2HSV)

    kernel = np.ones((1, 1), np.uint8)
    hsv = cv2.dilate(hsv, kernel, iterations=1)
    hsv = cv2.erode(hsv, kernel, iterations=1)
        # define range of white color in HSV
    # change it according to your need !
    sensitivity = 15
    lower_white = np.array([0,0,255-sensitivity], dtype=np.uint8)
    upper_white = np.array([255,sensitivity,255], dtype=np.uint8)
    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    cv2.imshow('mark', mask)
    text = pytesseract.image_to_string(mask, lang = 'eng')#eng
    print(text)
    # แสดงผล frame ที่เป็นขาวดำครับ
    cv2.putText(frame,text, (230, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    print(text)
    print(len(text))
    cv2.imshow('first_camera', frame)
    
    # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
#ออกจาก Loop While และจบการทำงาน
cap.release()
cv2.destroyAllWindows()

"""
from PIL import Image
import pytesseract
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
    im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #th3 = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    ret,th3 = cv2.threshold(im_gray,100,255,cv2.THRESH_BINARY)
    cv2.imshow('out_gray',th3)
    ROIimg = th3[200:300,100:400]
    cv2.rectangle(frame,(100,300),(400,200),(0,255,0),5)
    text = pytesseract.image_to_string(ROIimg, lang = 'eng')
    print(text)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text,(160,300), font, 2,(255,255,0),2) #สีขาว
    # แสดงผล frame ที่เป็นขาวดำครับ
    cv2.imshow('first_camera', frame)
    
    # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
#ออกจาก Loop While และจบการทำงาน
cap.release()
cv2.destroyAllWindows()
"""