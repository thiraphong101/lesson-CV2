#####################################################
#  CREATE BY Thiraphong Thiangphadung               # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #    
#           lesson8 Background Subtracton           #
#####################################################
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, flipCode=1)

    fgmask = fgbg.apply(frame)
    cv2.imshow('frame2', frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) #& 0xff
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
