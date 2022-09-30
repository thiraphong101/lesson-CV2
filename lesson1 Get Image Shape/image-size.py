#################################################
#  CREATE BY Thiraphong Thiangphadung           #  
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #
#  lesson1   Basic Image shape                  #
#################################################
import cv2
# read image
img = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)

# get dimensions of image
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)


import cv2
img1 = cv2.imread('test.png',0)
print(img1.shape)
