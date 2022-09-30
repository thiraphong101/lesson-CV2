####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         # 
#  lesson8 Haar-cascade Detection in OpenCV        #          
####################################################
import numpy as np
import cv2 as cv
#นำเข้า Cascade 
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
#อ่านไฟล์
img = cv.imread('Image.jpg')
#ปรับภาพให้เป็น Gray Color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    print(faces)
    print(faces.shape)
    print(faces.shape[0])
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()