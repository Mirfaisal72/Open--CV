import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(3)) # here 3 represents the property of width 
height = int(cap.get(4))# here 4 represents the property of height
while True:
    ret, frame = cap.read()
    image = np.zeros(frame.shape,np.uint8)
#Shrinking the image taken from frame into 1/4 of its original size
    smaller_img = cv2.resize(frame,(0,0), fx=0.5,fy= 0.5) #here fx represents rows and fy reprents columns
    image[:height//2,:width//2] = smaller_img
    image[height//2:,:width//2] = smaller_img
    image[:height//2,width//2:] = smaller_img
    image[height//2:,width//2:] = smaller_img
    cv2.imshow('Camera Feed', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()