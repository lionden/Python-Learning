import cv2
import numpy as np

lena = cv2.imread("B:\liond\Pictures\lena.png")
logo = np.zeros((200, 200, 3), np.uint8)
logo_mask = np.zeros((200, 200), np.uint8)

cv2.putText(logo, "Logo", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Logo", logo)

cv2.waitKey(0)