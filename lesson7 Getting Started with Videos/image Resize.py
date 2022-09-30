####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import cv2
import numpy as np
src = cv2.imread('cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED)
#percent by which the image is resized
scale_percent = 50
#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
# dsize
dsize = (width, height)
# resize image
#output = cv2.resize(src, dsize)
output = cv2.resize(src, (0,0), fx=0.50, fy=0.50)
print('Original Dimensions : ',src.shape)
print('Resized Dimensions : ',output.shape)
cv2.imwrite('D:/cv2-resize-image-50.png',output) 