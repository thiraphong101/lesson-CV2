import numpy as np
import cv2
cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2() #a background subtraction model is created
font = cv2.FONT_HERSHEY_SIMPLEX
while(1):
	ret, frame = cap.read()
	if ret == True:

		#modified part start
		#check if image is end or empty
		#do not proceed if image is empty
		##########################
		#if img is not None:
			#break
		#crop your ROI
		##########################
		#i am not sure where you want to crop but i assume you
		#want to crop at (100,100) as top left and (900,300) as bottom right
		ROIimg = frame[100:300,100:900]
		fgmask = fgbg.apply(ROIimg) # here is where you appply your image to background subtraction
		#modified part end

		kernel = np.ones((3,3),np.uint8)
		#remove noise
		th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
		dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations = 2)
		contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

		# roi=fgmask[100:300, 100:900] this line no longer needed as you apply croped image to background subtraction
		#cv2.rectangle(fgmask,(100,100),(900,300),(0,255,0),2)
		# you draw a rectange in frame to indicate ROI
		cv2.rectangle(frame,(100,100),(900,300),(0,255,0),2)

		for c in contours:
			if cv2.contourArea(c) > 800:#1600
				(x,y,w,h) = cv2.boundingRect(c)
				cv2.rectangle(frame, (x+100,y+100), (x+100+w, y+100+h), (255, 255, 0), 2) # here you add back the offset that you crop
				cv2.putText(frame,"Object" ,(x+102,y+h+110), font, 0.3, (255,255,255), 1)
		cv2.imshow('frame',frame)
		cv2.imshow('mask',fgmask)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
	else:
		print("break")
		break
cap.release()
cv2.destroyAllWindows()

#i never tested it out as i dont have opencv python with me. if my logic is correct then this should be working. i had modified a few part. please diff to check the difference.