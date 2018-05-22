import cv2
import numpy as np

image = cv2.imread('./images/girl.jpg')

cv2.imshow('Original image',image)
cv2.waitKey()

# creating our 3*3 kernel
kernel_3x3 = np.ones((3,3), np.float32) / 9

blurred = cv2.filter2D(image , -1, kernel_3x3)
cv2.imshow('3X3 Kernel Blurring', blurred)
cv2.waitKey()

# creating a 7x7 kernel matrix
kernel_7x7 = np.ones((7,7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7X7 Kernel Blurring', blurred2)
cv2.waitKey()

# MORE METHODS FOR IMAGE BLURRING

blur3 = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blurring', blur3)
cv2.waitKey()

median = cv2.medianBlur(image,5)
cv2.imshow('Median Blurring', median)
cv2.waitKey()

# Bilateral is very effective in noise control
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow('Bilateral BLurring', bilateral)
cv2.waitKey()

cv2.destroyAllWindows()