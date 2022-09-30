####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import numpy as np
import cv2

cap = cv2.VideoCapture('Minions_banana.mp4')
"""
ret = cap.set(3, 320)
ret = cap.set(4, 240)
"""
#fps ความเร็ว 25 frame/sec
fps = cap.get(cv2.CAP_PROP_FPS)  
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

#จำนวน frame Conut 5391.0 second
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('FRAME_COUNT', num_frames, 'second')

#ขนาดของ frame
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('frame_height：', frame_height, 'frame_width：', frame_width)

#Frame ปัจจุบัน 0.0
FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES) 
print('FRAME_NOW', FRAME_NOW)   

#Start Frame 100.0
frame_no = 100
cap.set(1, frame_no)
ret, frame = cap.read()
cv2.imshow('frame_no'+str(frame_no), frame)

#Frame ปัจจุบัน 101.0
FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
print('FRAME_NOW', FRAME_NOW)  

while cap.isOpened():
	ret, frame = cap.read()
	if ret == True:
		FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  
		print('FRAME_NOW', FRAME_NOW)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imshow('frame', gray)
		key = cv2.waitKey(25)
		if key == ord("q"):
			break
	# Break the loop
	else: 
		break

cap.release()
cv2.destroyAllWindows()


#   0  CV_CAP_PROP_POS_MSEC      Current position of the video file in milliseconds.
#   1  CV_CAP_PROP_POS_FRAMES    0-based index of the frame to be decoded/captured next.
#   2  CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
#   3  CV_CAP_PROP_FRAME_WIDTH   Width of the frames in the video stream.
#   4  CV_CAP_PROP_FRAME_HEIGHT  Height of the frames in the video stream.
#   5  CV_CAP_PROP_FPS           Frame rate.
#   6  CV_CAP_PROP_FOURCC        4-character code of codec.
#   7  CV_CAP_PROP_FRAME_COUNT   Number of frames in the video file.
#   8  CV_CAP_PROP_FORMAT        Format of the Mat objects returned by retrieve() .
#   9 CV_CAP_PROP_MODE           Backend-specific value indicating the current capture mode.
#   10 CV_CAP_PROP_BRIGHTNESS    Brightness of the image (only for cameras).
#   11 CV_CAP_PROP_CONTRAST      Contrast of the image (only for cameras).
#   12 CV_CAP_PROP_SATURATION    Saturation of the image (only for cameras).
#   13 CV_CAP_PROP_HUE           Hue of the image (only for cameras).
#   14 CV_CAP_PROP_GAIN          Gain of the image (only for cameras).
#   15 CV_CAP_PROP_EXPOSURE      Exposure (only for cameras).
#   16 CV_CAP_PROP_CONVERT_RGB   Boolean flags indicating whether images should be converted to RGB.
#   17 CV_CAP_PROP_WHITE_BALANCE Currently unsupported
#   18 CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)