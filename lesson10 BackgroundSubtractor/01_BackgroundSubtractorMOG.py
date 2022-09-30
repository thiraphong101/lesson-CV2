#####################################################
#  CREATE BY Thiraphong Thiangphadung               # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #    
#           lesson8 Background Subtracton           #
#####################################################
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()


while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, flipCode=1)

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    cv2.imshow('frame1', frame)
    k = cv2.waitKey(1) #& 0xff
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
