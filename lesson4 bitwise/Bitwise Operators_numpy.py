#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #     
#  lesson 4 image Operators                     #
#################################################
import cv2
import numpy as np

img1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img1, (150, 0), (300, 300), 255, -1)
cv2.imshow("Image 1", img1)

img2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img2, (150, 150), 90, 255, -1)
cv2.imshow("Image 2", img2)

rect_and_circle = cv2.bitwise_and(img1,img2)#(1*1=1 ,1*0=0)
cv2.imshow("AND operation",rect_and_circle)

rect_or_circle = cv2.bitwise_or(img1,img2)#(0+1=1 ,0+0=0 , 1+1=1 , 1+0=1)
cv2.imshow("OR operation",rect_or_circle)

rect_xor_circle = cv2.bitwise_not(img1)
cv2.imshow("NOT1 Operation",rect_xor_circle)

rect_xor_circle = cv2.bitwise_not(img2)
cv2.imshow("NOT2 Operation",rect_xor_circle)

rect_xor_circle2 = cv2.bitwise_xor(img1,img2)#(1+1=0)
cv2.imshow("XOR Operation",rect_xor_circle2)

cv2.waitKey(0)
cv2.destroyAllWindows()
