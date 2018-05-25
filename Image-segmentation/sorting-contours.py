import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

blank_image = np.zeros([image.shape[0], image.shape[1], 3])

# Create a copy of the original image
original_image = image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# FIND THE CANNY EDGES
edged = cv2.Canny(gray_image, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey()

# FIND THE CONTOURS AND COUNT THE NUMBERS
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print ("Numbers of Contours found :", len(contours))

# DRAW ALL CONTOURS
cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 2)
cv2.imshow('2 - All contours over blank images', blank_image)
cv2.waitKey()

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('2 - All contour', image)
cv2.waitKey()

cv2.destroyAllWindows()