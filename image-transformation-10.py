import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./images/scan.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

point_A = np.float32([[320,15],[700,215],[85,610],[530,780]])

point_B = np.float32([[0,0], [420,0],[0,594], [420,594]])

M = cv2.getPerspectiveTransform(point_A, point_B)

warped = cv2.warpPerspective(image, M,(420,594))

cv2.imshow('WarpedPerspective', warped)
cv2.waitKey()

cv2.destroyAllWindows()

## TODO DEVELOP YOUR OWN ALGORITHM TO FIND THE EDGE POINTS


