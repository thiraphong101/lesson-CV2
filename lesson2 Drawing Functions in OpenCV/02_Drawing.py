#################################################
#  CREATE BY Thiraphong Thiangphadung           #   
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #
#  lesson2 Drawing                              #
#################################################
# นำเข้า library
import numpy as np
import cv2 

# สร้างรูปภาพสีดำ
img = np.zeros((512,512,3), np.uint8)

# วาดเส้นสีน้ำเงินโดยมีความหนา 5 px
cv2.line(img,pt1=(15,20),pt2=(70,50),color=(255,0,0),thickness=5)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
# วาดวงกลมปิดสีแดง
cv2.circle(img,(200,200), 80, (0,0,255), -1)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
# วาดรูปวงรี 2 วง
cv2.ellipse(img,(200,200),(80,50),0,0,360,(0,255,0),-1)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
cv2.ellipse(img,(200,200),(80,50),45,0,360,(255,0,0),1)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
# วาดสี่เหลี่ยม (แบบไม่เต็มรูป) สีเขียว
cv2.rectangle(img,(15,20),(70,50),(0,255,0),3)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
# วาดสี่เหลี่ยมแบบเต็มรูป สีน้ำเงิน
cv2.rectangle(img,(115,120),(170,150),(255,0,0),-1)
cv2.imshow("Drawing", img)
cv2.waitKey(0)
# วาดข้อความลงไปในรูป
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello World!',(10,500), font, 1,(255,255,255),2)
# วาดรูปหลายเหลี่ยม
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))


#แสดงรูปภาพ
cv2.imshow("img",img)
cv2.waitKey(0)