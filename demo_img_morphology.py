import cv2
import numpy as np

img = cv2.imread("assets/beitie_book.png")
cv2.imshow('Original', img)

# erode via manual building kernel
size = (11, 11)
kernel = np.ones(size, np.uint8)
erode = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Erode', erode)

# erode via cv2.getStructuringElement
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, size)
erode2 = cv2.erode(img, kernel2, iterations=1)
cv2.imshow('Erode2', erode2)

# dilate
dilate = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Dilate', dilate)

# Morphology open: erode then dilate, can be used to remove noise on the background
img_open = cv2.imread('assets/morphology_open.png')
cv2.imshow('img_open', img_open)
morphology_open = cv2.morphologyEx(img_open, cv2.MORPH_OPEN, kernel)
cv2.imshow('morphology_open', morphology_open)

# Morphology close: dilate then erode, can be used to remove noise in the target
img_close = cv2.imread('assets/morphology_close.png')
cv2.imshow('img_close', img_close)
morphology_close = cv2.morphologyEx(img_close, cv2.MORPH_CLOSE, kernel)
cv2.imshow('morphology_close', morphology_close)

# Morphology gradient: original - erode, can be used to find the edges
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
gradient = cv2.morphologyEx(img_open, cv2.MORPH_GRADIENT, kernel3)
cv2.imshow('morphology_gradient', gradient)

# Morphology tophat: original - open, can be used to find the noise
tophat = cv2.morphologyEx(img_open, cv2.MORPH_TOPHAT, kernel3)
cv2.imshow('morphology_tophat', tophat)

# Morphology blackhat: close - original, can be used to find the noise in the target
blackhat = cv2.morphologyEx(img_close, cv2.MORPH_BLACKHAT, kernel3)
cv2.imshow('morphology_blackhat', blackhat)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()