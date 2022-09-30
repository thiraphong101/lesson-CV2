####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         # 
#  lesson8 Haar-cascade Detection in OpenCV        #          
####################################################
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print("faces="+str(len(faces)))
        cv2.putText(img, "FACES#: "+str(len(faces)), (x+1,y-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,255,0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            print("eyes="+str(len(eyes)))
            #cv2.putText(img, "EYES#: ", (ex,ey), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255,0,0), 1)
    cv2.imshow('face_detector', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
        break

cap.release()
cv2.destroyAllWindows()

