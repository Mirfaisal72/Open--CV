# Color Detection
import numpy as np
import cv2 
file = cv2.imread("Assets/chessboard.png")
file = cv2.resize(file,(0,0), fx=0.75,fy = 0.75)
gray_img = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)


#cornor detection algorithm
corners = cv2.goodFeaturesToTrack(gray_img,100,0.01,10)
#converting floating digit values into integer values
corners = np.int0(corners)
# the integrer values are in the type of arrays 
# we need to flatten those arrays to get the specific cornor values
for corner in corners:
    x,y = corner.ravel() # what ravel does is: [[[1,2,3]]] -> [1,2,3]
    cv2.circle(file,(x,y),5,(0,0,255),-1)

# Drawing lines between corners
for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(file, corner1, corner2, color, 1)

cv2.imshow("Chessboard", file)
cv2.waitKey(0)
cv2.destroyAllWindows()
