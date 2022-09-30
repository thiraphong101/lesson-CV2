#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 3 ROI                                 #
#################################################
import cv2
import numpy as np
image = cv2.imread("flag.png")
cols, rows, ch = image.shape
#print px ภายในภาพ
print(image)
#print px ตำแหน่งภายในภาพ
print(image[cols-1, rows-1])
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

