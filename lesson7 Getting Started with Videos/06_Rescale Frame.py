####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         #  
#  lesson 7 Getting Started with Videos            #          
####################################################
import cv2
cap = cv2.VideoCapture(0)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
while True:
    rect, frame = cap.read()
    frame75 = rescale_frame(frame, percent=75)
    cv2.imshow('frame75', frame75)
    frame20 = rescale_frame(frame, percent=20)
    cv2.imshow('frame20', frame20)
    frame50 = rescale_frame(frame, percent=50)
    cv2.imshow('frame50', frame50)



    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()