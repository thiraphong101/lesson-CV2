####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
"""
ในการระบุ FourCC code โดยมี video codec ที่ทำงานได้โดยไม่ได้ลง video codec เพิ่มดังนี้
บน Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2
บน Windows: DIVX, XVID
 กำหนด FourCC code"""
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#cv2.VideoWriter(ชื่อไฟล์วิดีโอ,fourcc, จำนวนเฟรมต่อวินาที, (ขนาดแกน x,ขนาดแกน y))
#ใช้คำสั่ง cv2.VideoWriter() ในการอัดวิดีโอลงไฟล์ครับ
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
"""
อธิบายคำสั่งเพิ่มเติม
คำสั่ง isOpened() เป็นคำสั่งสำหรับตรวจเช็คว่าทุกอย่างพร้อมใช้งานหรือไม่ โดยจะคืนค่าบูลีน (True/False)
"""