import cv2

image = cv2.imread('./images/deepak.jpeg')
cv2.imshow('Original',image)
cv2.waitKey(1000)

# destroy the window with window name original
cv2.destroyWindow('Original')

# Convert into grey scale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Scaled',grey_image)
cv2.waitKey(1000)

cv2.destroyWindow('Grey Scaled')

grey_image2 = cv2.imread('./images/deepak.jpeg',0)
cv2.imshow('Grayscale',grey_image2)
cv2.waitKey(1000)

