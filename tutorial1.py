# loading an image, resizing and rotating an image
import cv2
img = cv2.imread("C:/Users/MIR FAISAL/Documents/Python/Machine Learning/Open - CV/EYE.jpg",-1)
img = cv2.resize(img,(400,400))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()