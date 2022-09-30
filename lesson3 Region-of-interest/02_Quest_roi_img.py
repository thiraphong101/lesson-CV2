#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 3 ROI                                 #
#################################################

import numpy as np
import cv2

img = cv2.imread("t1.jpg",cv2.IMREAD_COLOR)
#Step 2  กรอบ ROI
roi =img [213:434,255:505] #y1:y2,x1:x2
roi2 =img [0:213,508:770] #y1:y2,x1:x2
#Step 1  rectangle for ROI
cv2.rectangle(img,(255,213),(505,434),(0,0,255),4)#(x,y),(w,h)
cv2.rectangle(img,(508,0),(770,213),(255,0,255),4)#(x,y),(w,h)
#Step 3  แสดง ROI บนภาพ
img[213-213:434-213,255-255:505-255]=roi
img[0+213:213+213,508-508:770-508]=roi2
#print(roi.shape)
print(img.shape)
cv2.imshow("image",img)
cv2.imwrite("roi2.png",roi)
cv2.imshow("roi",roi)
cv2.imshow("roi2",roi2)
cv2.imwrite("image.png",img)

#cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows