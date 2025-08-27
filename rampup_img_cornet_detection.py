import cv2
import numpy as np

img = cv2.imread('assets/sudoku.png')
cv2.imshow('img',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
cornerHarris
cornerHarris(src, blockSize, ksize, k)
blockSize: 检测窗口大小. 值越大, 检测出的角占的区域越大
ksize:  Sobel算子核大小. 值越小, 检测出的角越多, 但准确率越低
k: 权重系数, 一般取0.02~0.04. 值越小, 检测出的角越多, 但准确率越低
'''
harris_dst = cv2.cornerHarris(gray, 2, 3, 0.03)
harris = img.copy()
harris[harris_dst > 0.01 * harris_dst.max()] = [0,0,255]
cv2.imshow('harris',harris)

'''
Shi-Tomasi角点检测
goodFeaturesToTrack(src,maxCorners, qualityLevel, minDistance)
maxCorners: 最多检测的角点数量, 0表示不限制
qualityLevel: 角点检测的精度. 值越小, 检测到的角点越少
minDistance: 检测到的角点之间的最小距离

Optional:
useHarrisDetector: 是否使用Harris角点检测算法
'''
corners = cv2.goodFeaturesToTrack(gray, 0, 0.01, 10)
corners = np.int32(corners)
shitomasi = img.copy()
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(shitomasi, (x,y), 3, (0,0,255), -1)

cv2.imshow('shitomasi',shitomasi)

'''
SIFT
Create SIFT object
Detect keypoints
Draw keypoints
'''
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray)
sift_img = img.copy()
cv2.drawKeypoints(gray, kp, sift_img)
cv2.imshow('sift', sift_img)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()