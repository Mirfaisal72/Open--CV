import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    width = int(cap.get(3))
    heigth = int(cap.get(4)) 

    cv2.imshow("Camera feed", frame)

    if(cv2.waitKey(1) == ord('x')):
        break
cap.release()
cv2.destroyAllWindows()
