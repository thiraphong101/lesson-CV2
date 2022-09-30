#################################################
#  CREATE BY Thiraphong Thiangphadung           #   
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #
#  lesson2 Drawing                              #
#################################################
# นำเข้า library
import numpy as np
import cv2

# สร้างรูปภาพสีดำ ขนาด 512X512
img = np.zeros((512,512,3), np.uint8)

# วาดสี่เหลี่ยมแบบเต็มรูป สีน้ำเงิน
cv2.rectangle(img,(2,511),(500,400),(255,0,0),-1)
# วาดข้อความลงไปในรูป
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Thiraphong Thiangphadung',(40,470), font, 1,(255,255,255),2)
cv2.rectangle(img,(2,510),(500,400),(0,255,0),3)
print(img.shape)
#แสดงรูปภาพ
cv2.imshow("img",img)
cv2.waitKey(0)