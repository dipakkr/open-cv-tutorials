import cv2
import numpy as np

image = cv2.imread('./images/girl.jpg', 0 )

height, width = image.shape

sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize= 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize= 5)

cv2.imshow('Original', image)
cv2.waitKey(0)

cv2.imshow('Sobel X',sobel_x)
cv2.waitKey()

cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey()
