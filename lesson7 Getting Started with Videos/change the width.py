####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import cv2
import numpy as np
src = cv2.imread('cv2-resize-image-original.png', cv2.IMREAD_UNCHANGED)
# set a new width in pixels
new_width = 300
# dsize
dsize = (new_width, src.shape[0])
# resize image
output = cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
print('Original Dimensions : ',src.shape)
print('Resized Dimensions : ',output.shape)
cv2.imwrite('D:/cv2-resize-image-width.png',output) 