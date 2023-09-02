# Image Manipulation
import cv2
import random
img = cv2.imread("C:/Users/NAME/Documents/Python/Machine Learning/Open - CV/EYE.jpg",1)
img = cv2.resize(img,(400,400))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
'''print("The pixels of Image are: " , img) # prints a numpy array
print(img.shape) # gives the rows, columns , channels
 # looking at the frst row of image:
print("_______________")
#print(img[2500][1900])
#Randomly setting up pixels to change colours 
for i in range(100): #Accessing the rows 
    for j in range(img.shape[1]): # Accessing the columns (Pixels)
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]'''
tag = img[50:80,90:120]
img[230:260,350:380] = tag
cv2.imshow('Altered Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows        
