#####################################################
#  CREATE BY Thiraphong Thiangphadung               # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #    
#           lesson8 Background Subtracton           #
#####################################################
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

counter=0
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    cv2.imshow('frame2', frame)
    counter+=1
    print(counter)

    k = cv2.waitKey(1)  # & 0xff
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
