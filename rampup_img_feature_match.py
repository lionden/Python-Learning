import cv2
import numpy as np
from scipy.fft import dst

# search img from the img_beitie
# img = cv2.imread('assets/OpenCV_logo.png')
# img_beitie = cv2.imread('assets/lena-with-opencv-logo.png')
img = cv2.imread('assets/beitie_zao.png')
img_beitie = cv2.imread('assets/beitie_part1.png')
cv2.imshow('img',img)
cv2.imshow('img_beitie',img_beitie)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_beitie = cv2.cvtColor(img_beitie, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp, desc = sift.detectAndCompute(gray, None)
kp_beitie, desc_beitie = sift.detectAndCompute(gray_beitie, None)


'''
BFMatcher: Brute-force matcher
Create matcher
compare the features
Draw the matches
'''
bf = cv2.BFMatcher(cv2.NORM_L1)
matches = bf.match(desc, desc_beitie)
result_bf = cv2.drawMatches(img, kp, img_beitie, kp_beitie, matches, None)
cv2.imshow('BFMatcher',result_bf)


'''
FLANN: Fast Library for Approximate Nearest Neighbors
Create matcher
compare the features
Draw the matches
'''
flann = cv2.FlannBasedMatcher_create()
matches = flann.match(desc, desc_beitie)
result_flann = cv2.drawMatches(img, kp, img_beitie, kp_beitie, matches, None)
cv2.imshow('FLANN',result_flann)

# KNN match
matches_knn = flann.knnMatch(desc, desc_beitie, k=2)
good = []
for i, (m, n) in enumerate(matches_knn):
    if m.distance < 0.7 * n.distance:
        good.append(m)

# search image via homography
if len(good) < 4:
    print('Not enough matches are found - %d/%d' % (len(good), 4))
    exit()

srcPts = np.float32([kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
dstPts = np.float32([kp_beitie[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
H, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)

h, w = img.shape[:2]
pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
dst = cv2.perspectiveTransform(pts, H)

cv2.polylines(img_beitie, [np.int32(dst)], True, (0, 0, 255))

result_knn = cv2.drawMatchesKnn(img, kp, img_beitie, kp_beitie, [good], None)
cv2.imshow('FLANN_knn',result_knn)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()