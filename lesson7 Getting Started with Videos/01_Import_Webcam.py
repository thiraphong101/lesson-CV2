####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import numpy as np
import cv2
cap = cv2.VideoCapture("pedestrians.avi")#('http://10.220.1.77:40000/videostream.cgi?user=admin&pwd=888888')#("http:admin:1234@10.211.50.171/cgi-bin/mjpeg?stream=0")#
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # แสดงผล frame ที่เป็นสี
    cv2.imshow('first_camera', frame)
    # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
#ออกจาก Loop While และจบการทำงาน
cap.release()
cv2.destroyAllWindows()

