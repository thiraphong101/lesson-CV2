####################################################
#  CREATE BY Thiraphong Thiangphadung              #
# เลขประจำตัว 593684 แผนก หทปอ-ห. ฝ่าย อปอ.         # 
#  lesson8 Haar-cascade Detection in OpenCV        #          
####################################################
import cv2
import sys

imagePath = "people_with_phones.png"

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print("[INFO] Found {0} Faces.".format(len(faces)))

for (i,(x,y,w,h)) in enumerate(faces):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, "FACES#: "+str(i+1), (x+1,y-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,255,0), 1)
    roi_color = image[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite("ID" + str(i) + '_faces.jpg', roi_color)

status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
for f in range(i+1) :
    image_face = cv2.imread("ID" + str(f) + '_faces.jpg')
    cv2.imshow('id'+str(f), image_face)
cv2.imshow("faces_detected.jpg", image)
cv2.waitKey(0)  # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
cv2.destroyAllWindows()