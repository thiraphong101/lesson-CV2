####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import numpy as np
import cv2
import time
import os
count = 0
path = 'E:\\อบรม opencv\\อบรม opencv 2564\\Lesson_part1\\lesson7 Getting Started with Videos'
##############
cap = cv2.VideoCapture(0)
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
    #cv2.imwrite("Frame{}.png".format(count),frame)
    cv2.imwrite(os.path.join(path,"Frame{}.png".format(count)),frame)
    print("Save Img"+str(count))
    time.sleep(0.5)
    count += 1
    if count >= 5 :
    	count = 0
    # แสดงผล frame ที่เป็นขาวดำครับ
    #cv2.imshow('first_camera', frame)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Save Img'+str(count),(10,60), font, 2,(255,0,255),3)

    cv2.imshow('first_camera', frame)
    # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
#ออกจาก Loop While และจบการทำงาน
cap.release()
cv2.destroyAllWindows()

