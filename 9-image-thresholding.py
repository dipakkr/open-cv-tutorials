import cv2
import numpy as np

image = cv2.imread('./images/girl.jpg')
cv2.imshow('Original', image)

# Values below 127 goes to 0 (black), everything above goes to 255 ( white )

ret, thresh1 = cv2.threshold(image,127,255, cv2.THRESH_BINARY)
cv2.imshow('1 Threshold Binary', thresh1)

# Values below 127 go to 255 and values above 127 goes to 0
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('2 Threshold Binary Inversion', thresh2)

cv2.waitKey()