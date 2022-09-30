import cv2
import numpy as np
blank = np.zeros((500, 500, 3), dtype = "uint8")
# display the blank image first
blank[:] = 0, 255, 0 # green
cv2.imshow("Green", blank)
cv2.waitKey(0)
cv2.destroyAllWindows()