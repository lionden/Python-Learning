import cv2
import numpy as np

img = cv2.imread("D:\Repos_GitHub\opencv-4.1.0\samples\data\pic3.png")
cv2.imshow("img", img)

# sobel, 需分别对x,y求导.
img_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0)
cv2.imshow("img_sobel", img_sobel)
img_sobel2 = cv2.Sobel(img, cv2.CV_64F, 0, 1)
cv2.imshow("img_sobel2", img_sobel2)

dst = cv2.add(img_sobel, img_sobel2)
cv2.imshow("img_sobel+img_sobel2", dst)

# scharr, 支持对较为细的图像进行求导
img_scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
img_scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
cv2.imshow("img_scharr_x", img_scharr_x)
cv2.imshow("img_scharr_y", img_scharr_y)

dst = cv2.add(img_scharr_x, img_scharr_y)
cv2.imshow("img_scharr+img_scharr", dst)

# laplacian, 支持同时对x,y求导, 但使用前需进行降噪处理
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("laplacian", laplacian)

# canny, 全能型边缘检测算法
canny = cv2.Canny(img, 100, 200)
cv2.imshow("canny", canny)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()