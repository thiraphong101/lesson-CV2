#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #           
#  lesson 5 Getting Started with Images         #
################################################# 
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
