####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import numpy as np
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)
#width = 640
ret = cap.set(3, 320)
#height = 480
ret = cap.set(4, 240)
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
    # แสดงผล frame ที่เป็นขาวดำครับ

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p") + ' DateTime',(5,20), font, 0.7,(255,255,255),1)
    cv2.imshow('first_camera', frame)
    # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
#ออกจาก Loop While และจบการทำงาน
cap.release()
cv2.destroyAllWindows()

# วาดข้อความลงไปในรูป
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(frame,a,(10,500),font, 0.7,(255,255,255),1)