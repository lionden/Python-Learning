import cv2
import numpy as np

window_none = "color_converter"
cv2.namedWindow(window_none, cv2.WINDOW_AUTOSIZE)

img = cv2.imread("B:\liond\Pictures\lena.png")
cv2.imshow("original", img)

color_spaces=[cv2.COLOR_RGB2BGR, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YUV]
cv2.createTrackbar("color_space", window_none, 0, len(color_spaces)-1, lambda x: None)

while True:
    color_space_index = cv2.getTrackbarPos("color_space", window_none)
    cv2_img = cv2.cvtColor(img, color_spaces[color_space_index])
    cv2.imshow(window_none, cv2_img)
    if cv2.waitKey(100) == ord('q'):
        break

cv2.destroyAllWindows()