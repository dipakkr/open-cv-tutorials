import cv2

capture = cv2.VideoCapture(0)

def sketch(image):

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # 4 Do an Invert binarize the images
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


while True:
    ret, frame = capture.read()
    cv2.imshow("Live Sketcher Application", sketch(frame))

    if cv2.waitKey(1) == 13 : # 13 is the Enter key
        break

capture.release()
cv2.destroyAllWindows()

