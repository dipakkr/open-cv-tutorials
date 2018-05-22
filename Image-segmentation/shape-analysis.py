import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')

cv2.imshow('Input Image', image)
cv2.waitKey()

# Gray Scale the Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# FIND CANNY EDGES
edged = cv2.Canny(gray_image, 30,200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey()

# Finding the  contours
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges after contouring', edged)
cv2.waitKey()

print ("Number of Contours found " + str(len(contours)))

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0),3)

cv2.imshow("Contours", image)
cv2.waitKey()
cv2.destroyAllWindows()