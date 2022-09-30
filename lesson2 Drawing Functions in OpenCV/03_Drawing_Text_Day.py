#################################################
#  CREATE BY Thiraphong Thiangphadung           #   
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #
#  lesson2 Drawing                              #
#################################################
# นำเข้า library
import numpy as np
import cv2
import time
#TIME
timeis = time.localtime()
a = time.strftime('%A %d %B %Y, %H:%M:%S', timeis)
print(a)

# สร้างรูปภาพสีดำ
img = np.zeros((512,512,3), np.uint8)
# วาดข้อความลงไปในรูป
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,a,(10,500), font, 0.7,(255,255,255),2) #สีขาว

#แสดงรูปภาพ
cv2.imshow("img",img)
cv2.waitKey(0)