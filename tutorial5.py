#Color and Color manipulation

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    width = int(cap.get(3))
    heigth = int(cap.get(4)) 
    #BGR TO HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Retreiving Specific Color
    lower_bound = np.array([90,50,50])
    upper_bound = np.array([130,255,255])
    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Camera feed", result)
    cv2.imshow("Mask feed", mask)

    if(cv2.waitKey(1) == ord('x')):
        break
cap.release()
cv2.destroyAllWindows()
