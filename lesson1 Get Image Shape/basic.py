#################################################
#  CREATE BY Thiraphong Thiangphadung           #  
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #
#  lesson1   Basic Image shape                  #
#################################################
import cv2
import numpy as np
img = cv2.imread('python.png')
px = img[100,100]
print( "px = ",px )

# accessing only blue pixel
blue = img[100,100,0] #B [100,100,1] #R [100,100,2]
print( "blue = ",blue )

img[100,100] = [255,255,255]
print( "modify = ",img[100,100] )

# accessing RED value
Red = img.item(10,10,2)
print( "Red = ",Red )

# modifying RED value
img.itemset((10,10,2),100)
modify = img.item(10,10,2)
print(  "modify = ",modify )

print( "shape = ",img.shape )

print( "size = ",img.size ) #W*H*3

print( "type = ",img.dtype )