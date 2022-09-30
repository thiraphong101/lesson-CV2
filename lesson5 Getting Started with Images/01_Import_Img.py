#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #           
#  lesson 5 Getting Started with Images         #
################################################# 
import numpy as np
import cv2
#อ่านภาพ จาก File
img = cv2.imread('messi5.jpg')
#แสดงภาพ
cv2.imshow('img',img)
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
print(img)
print(img.shape)
print (img.size)
print (img.dtype)
#จบการทำงาน
cv2.waitKey(0)
cv2.destroyAllWindows()



