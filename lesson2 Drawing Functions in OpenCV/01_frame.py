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
#img[:, :] = [255, 255, 255]
#แสดงรูปภาพ
cv2.imshow("img",img)
cv2.waitKey(0)