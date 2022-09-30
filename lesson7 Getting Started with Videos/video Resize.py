####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    #percent by which the image is resized
    scale_percent = 50
    #calculate the 50 percent of original dimensions
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # resize image
    output2 = cv2.resize(frame, (0,0), fx=0.50, fy=0.50)
    output = cv2.resize(frame, dsize)
    cv2.imshow('frame',output)
    cv2.imshow('frame2',output2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
