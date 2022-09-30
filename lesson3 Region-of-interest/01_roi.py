#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 3 ROI                                 #
#################################################

import numpy as np
import cv2

img = cv2.imread("t1.jpg",cv2.IMREAD_COLOR)
"""
#Step 2 กรอบ ROI
roi =img [213:434,255:505] #y1:y2,x1:x2
#Step 1 rectangle 
cv2.rectangle(img,(255,213),(505,434),(0,0,255),4)#(x,y),(w:h)
#Step 3 ย้าย ROI บน Frame
img[213-213:434-213,255-255:505-255]=roi
"""
cv2.rectangle(img,(255,213),(505,434),(0,0,255),4)#(x,y),(w,h)
roi =img [213:434,255:505] #y1:y2,x1:x2

img[213: 434,255+265:505+265]=roi  #y1:y2,x1:x2
#print(roi.shape)
print(img.shape)
cv2.imshow("roi",roi)
cv2.imshow("image",img)
"""
cv2.imwrite("image.png",img)
cv2.imshow("roi",roi)
"""

cv2.waitKey(0)
cv2.destroyAllWindows