import cv2

image = cv2.imread('./images/girl.jpg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('original', image)

cv2.imshow('Smaller',smaller)
cv2.imshow('Larger',larger)
cv2.waitKey()
cv2.destroyAllWindows()