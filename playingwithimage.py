import cv2
import numpy as np

 # input image
image = cv2.imread('./images/tajm.JPG')
cv2.imshow('Original',image)
cv2.waitKey()

# BGR values for the first (50,90) pixel
B, G, R = image[50,90]
print B,G,R

# see what happens when we convert this to grayscale
gray_image = cv2.imread('./images/tajm.JPG',0)
cv2.imshow('Grey Image',gray_image)
cv2.waitKey()
print gray_image.shape


# H : 0 - 180, S : 0 - 255, V : 0 - 255

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV IMAGE',hsv_image)
cv2.waitKey()

cv2.imshow('HUE CHANNEL',hsv_image[:, :, 0])
cv2.waitKey()

cv2.imshow('SATURATION CHANNEL',hsv_image[:, :, 1])
cv2.waitKey()

cv2.imshow('VALUE CHANNEL',hsv_image[:,:,2])
cv2.waitKey()
