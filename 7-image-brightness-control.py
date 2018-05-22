import cv2
import numpy as np

image = cv2.imread('./images/girl.jpg')

Matrix = np.ones(image.shape, dtype="uint8") * 75

added = cv2.add(image,Matrix)
cv2.imshow("Added",added)

subtracted  = cv2.subtract(image, Matrix)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
