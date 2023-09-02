# Drawing lines Images circles and text
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) 
    height = int(cap.get(4))
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    img = cv2.line(img,(0,height),(width,0),(0,255,0),10)
    img = cv2.rectangle(img,(100,100),(200,200),(0,0,255),5)
    img = cv2.circle(frame,(100,100),50,(0,0,255),-1) #-1 for filling in the circle colour
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, "Open CV project",(100,height -10), font,2,(0,0,255),5,cv2.LINE_AA)

    cv2.imshow('Camera Feed', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()