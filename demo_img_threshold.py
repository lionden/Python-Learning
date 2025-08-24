import cv2
import numpy as np

lena = cv2.imread("assets/lena.png")
cv2.imshow("lena",lena)

gray = cv2.cvtColor(lena,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

# binary
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("binary",binary)

# truncate, 削峰
ret, truncate = cv2.threshold(gray, 100, 255, cv2.THRESH_TRUNC)
cv2.imshow("truncate",truncate)

# tozero
ret, tozero = cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO)
cv2.imshow("tozero",tozero)

# adaptive threshold
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)
cv2.imshow("adaptive",adaptive)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()