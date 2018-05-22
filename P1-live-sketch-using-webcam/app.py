import cv2
import numpy as np

# Initialize the web cam, store the image

capture = cv2.VideoCapture(0)

def sketch(image):

    # 1 Convert Image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2 Now, Clean the Image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

    # 3 Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # 4 Do an Invert binarize the images
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


while True:
    ret, frame = capture.read()
    cv2.imshow("Live Sketcher Application", sketch(frame))

    if cv2.waitKey(1) == 13 : # 13 is the Enter key
        break

# Release the camera and close windows
capture.release()
cv2.destroyAllWindows()


# Play with the returned video feed by changing the return statement