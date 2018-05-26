import cv2
import numpy as np

image = cv2.imread('../images/someshapes.jpg')

blank_image = np.zeros(image.shape)
original_image = image.copy()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray_image, 100, 500)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 2)
cv2.imshow('2 - All contours over blank images', blank_image)
cv2.waitKey()


def sort_x_cord(contours):

    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return int(M['m10'] / M['m00'])
    else:
        pass


def label_centroid(image, c):
    m = cv2.moments(c)
    cx = int(m['m10'] / m['m00'])
    cy = int(m['m01'] / m['m00'])
    cv2.circle(image, (cx,  cy), 10, (0, 0, 255), -1)
    return image


for (i, c) in enumerate(contours):
    orig = label_centroid(image, c)

cv2.imshow("Centroid Centre", image)
cv2.waitKey()

# Sort the contours by left to right using our x_cord_contour function
contours_L2R = sorted(contours, key=sort_x_cord, reverse=False)

for (i, c) in enumerate(contours_L2R):
    cv2.drawContours(original_image, [c], -1, (0, 0, 255), 3)
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(original_image, str(i + 1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('6 - Left to Right Contour', original_image)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)

    # Let's now crop each contour and save these images

    # cropped_contour = original_image[y:y + h, x:x + w]
    # image_name = "output_shape_number_" + str(i + 1) + ".jpg"
    # print image_name
    # cv2.imwrite(image_name, cropped_contour)

cv2.destroyAllWindows()