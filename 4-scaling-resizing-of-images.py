import cv2
import numpy as np

image = cv2.imread('./images/girl.jpg')

# image size is 3/4th
scaled_image = cv2.resize(image,None, fx=0.75, fy=0.75)
cv2.imshow('Scaling - Lineae Interpolation',scaled_image)
cv2.waitKey()

# doubling th image size
img_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation',img_scaled)
cv2.waitKey()

# custom resize of image
img_scaled = cv2.resize(image,(400,200),interpolation=cv2.INTER_AREA)
cv2.imshow('Custom Rescaled Image',img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()