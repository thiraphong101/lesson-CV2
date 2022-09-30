#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #           
#  lesson 5 Getting Started with Images         #
################################################# 
import cv2
# read two images
src1 = cv2.imread('image1.png', cv2.IMREAD_COLOR)
src2 = cv2.imread('image2.png', cv2.IMREAD_COLOR)
# add or blend the images
dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
# show the output image
cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()