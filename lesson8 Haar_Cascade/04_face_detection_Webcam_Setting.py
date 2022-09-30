####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         # 
#  lesson8 Haar-cascade Detection in OpenCV        #          
####################################################
import numpy as np
import cv2

def nothing(x):
    pass

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

def rescale_frame(frame, percent=120):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

cv2.namedWindow("Setting_Face")
cv2.createTrackbar("Scale","Setting_Face",11,20,nothing)
cv2.createTrackbar("Neighbours","Setting_Face",5,20,nothing)
cv2.namedWindow("Setting_Fire")
cv2.createTrackbar("Scale","Setting_Fire",11,20,nothing)
cv2.createTrackbar("Neighbours","Setting_Fire",5,20,nothing)

cap = cv2.VideoCapture(0)
while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fa_scale = cv2.getTrackbarPos("Scale","Setting_Face")
    fa_neighbours = cv2.getTrackbarPos("Neighbours","Setting_Face")
    fi_scale = cv2.getTrackbarPos("Scale","Setting_Fire")
    fi_neighbours = cv2.getTrackbarPos("Neighbours","Setting_Fire")


    faces = face_cascade.detectMultiScale(gray, fa_scale/10, fa_neighbours)
    for (i,(x,y,w,h)) in enumerate(faces):
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print("faces="+str(len(faces)))
        print(faces.shape)
        print(i+1)
        print(img.shape)

        cv2.rectangle(img, (x-1,y-30), (x+w+1, y-1), (255,0,0), -1)
        cv2.putText(img, "FACES : ID " + str(i+1), (x+1,y-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255,255,255), 1)
    fires = fire_cascade.detectMultiScale(gray, fi_scale/10, fi_neighbours)
    for (f,(x,y,w,h)) in enumerate(fires):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        print("fires="+str(len(fires)))
        print(fires.shape)
        print(f+1)
        cv2.rectangle(img, (x-1,y-30), (x+w+1, y-1), (0,0,255), -1)
        cv2.putText(img, "FIRES : ID " + str(f+1), (x+1,y-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255,255,255), 1)   


    cv2.rectangle(img, ((640,img.shape[0] -25)),(450, img.shape[0]), (0,0,255), -1)
    cv2.putText(img, "Number of fires: " +str(len(fires)), (460,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    
    cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
    cv2.putText(img, "Number of faces detected: " + str(len(faces)), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)    
    
    frame120 = rescale_frame(img, percent=120)

    cv2.imshow('face_detector', frame120)
    if cv2.waitKey(1) & 0xFF == ord('q'): # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
        break

cap.release()
cv2.destroyAllWindows()

