####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         # 
#  lesson8 Haar-cascade Detection in OpenCV        #          
####################################################
import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
 
image = cv.imread('test.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
# Print ttpe ในการคำนวนทางคณิตศาตร์
print (type(faces))
# len() == funchionใช้นับจำนวน 
if len(faces) == 0:
    print ("No faces found")
 
else:
    print (faces)
    print (faces.shape)
    print ("Number of faces detected: " + str(faces.shape[0]))
 
    for (i,(x,y,w,h)) in enumerate(faces): #enumerate มีประโยชน์เวลาที่เราต้องการให้เวลาที่ใช้ for เพื่อวนซ้ำอยู่มีตัวเลขบางอย่างที่ช่วยนับจำนวนรอบ
        cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1) 
        cv.putText(image, "FACE#: " + str(i+1), (x+1,y-10), cv.FONT_HERSHEY_TRIPLEX, 0.5,  (0,255,0), 1)

    
    cv.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    #print(image.shape[0])
    cv.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
 
    cv.imshow('Image with faces',image)
    cv.waitKey(0)
    cv.destroyAllWindows()