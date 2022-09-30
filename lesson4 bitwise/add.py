#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 4 image Operators                     #
#################################################
"""
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
add = img1+img2
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
add = cv2.add(img1,img2)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

