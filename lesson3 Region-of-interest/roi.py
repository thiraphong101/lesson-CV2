#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 3 ROI                                 #
#################################################
import cv2
import numpy as np
image = cv2.imread("red_panda.jpg")
print(image.shape)
cols, rows, ch = image.shape
#Roi = [y1:y2,x1:x2]
#roi = image[0: rows, 0: cols]
roi = image[100: 280, 150: 320]
cv2.rectangle(image,(150,100),(320,280),(255,0,0),2)
cv2.imshow("Panda", image)
cv2.imshow("Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

