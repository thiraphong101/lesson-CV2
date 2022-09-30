#################################################
#  CREATE BY Thiraphong Thiangphadung           #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.      #           
#  lesson 5 Getting Started with Images         #
################################################# 
import numpy as np
import cv2
#อ่านภาพ จาก File
img = cv2.imread('Image.jpg',0)
#แสดงภาพ
cv2.imshow('img',img)

#รอรับ KEY
KEY = cv2.waitKey(0)
# รอ ESC key เพื่อออกจากระบบ
if KEY == 27: 
	cv2.destroyAllWindows()
elif KEY == ord('s'): 
# รอ 'S' key เพื่อบันทึก และออกจากระบบ
	cv2.imwrite('Image_gray5465.jpg',img)
	cv2.destroyAllWindows()


