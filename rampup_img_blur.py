import cv2
import numpy as np

img = cv2.imread('lena.png')
cv2.imshow('Original',img)

kernal = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernal)
cv2.imshow('Averaging',dst)

# Blur, 均值滤波
dst2 = cv2.blur(img, (5, 5))
cv2.imshow('Blur',dst2)

# 高斯滤波, 高斯噪音: 噪点与原图像的色值相近
gaussianBlur = cv2.GaussianBlur(img,(5,5), 1)
cv2.imshow('GaussianBlur',gaussianBlur)

ocr = cv2.imread("E:\Assets\ComputerVision\\45562e4360dd495db1b9fc187aaea0e5.png")
cv2.imshow('ocr',ocr)

# 中值滤波, 椒盐噪音: 随机的白点或黑点
medianBlur = cv2.medianBlur(ocr,3)
cv2.imshow('medianBlur',medianBlur)

# BilateralFilter, 双边滤波, 美颜
bilateralFilter = cv2.bilateralFilter(img,9,20,50)
cv2.imshow('bilateralFilter',bilateralFilter)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()