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

# Split the images in R,G,B
B,G,R = cv2.split(image)

print B.shape
cv2.imshow("BLUE",B)
cv2.imshow("GREEN",G+100)
cv2.imshow("RED",R)
cv2.waitKey()

zeroes = np.zeros(image.shape[:2], dtype="uint8")

cv2.imshow("RED",cv2.merge([zeroes,zeroes,R]))
cv2.imshow("Green",cv2.merge([zeroes,G,zeroes]))
cv2.imshow("Blue",cv2.merge([B,zeroes,zeroes]))

cv2.waitKey()

image.shape[:2]
