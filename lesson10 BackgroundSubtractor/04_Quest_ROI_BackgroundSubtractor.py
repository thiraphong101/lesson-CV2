#####################################################
#  CREATE BY Thiraphong Thiangphadung               # 
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.          #    
#           lesson8 Background Subtracton           #
#####################################################
import numpy as np
import cv2
cap = cv2.VideoCapture("Highway Surveillance.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
	ret, frame = cap.read()
	ROIimg = frame[400:700,100:1000]
	fgmask = fgbg.apply(ROIimg)
	kernel = np.ones((3,3),np.uint8)
	th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
	dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations = 2)
	contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.rectangle(frame,(100,700),(1000,400),(0,255,0),2)
	for c in contours:
		if cv2.contourArea(c) > 1600: 
			(x,y,w,h) = cv2.boundingRect(c)
			cv2.rectangle(frame, (x+100,y+400), (x+100+w, y+400+h), (255, 255, 0), 2)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,'object',(x+100,y+400), font, 1,(255,255,255),2)
	cv2.imshow('frame',frame)
	cv2.imshow('frame2',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()