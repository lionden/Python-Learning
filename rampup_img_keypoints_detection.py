import cv2
import numpy as np

img = cv2.imread('assets/sudoku.png')
cv2.imshow('img',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
SIFT
Create SIFT object
Detect keypoints
Draw keypoints
'''

# detect keypoints
# sift = cv2.xfeatures2d.SIFT_create()  # OR below code 👇👇👇
sift = cv2.SIFT_create()
kp = sift.detect(gray)
sift_img = img.copy()
cv2.drawKeypoints(gray, kp, sift_img)
cv2.imshow('sift', sift_img)

# detect and compute keypoints
kp, desc = sift.detectAndCompute(gray, None)    # ★★★
sift_img2 = img.copy()
cv2.drawKeypoints(gray, kp, sift_img2)
cv2.imshow('sift2', sift_img2)


'''
SURF, faster than SIFT
Create SURF object
Detect keypoints
Draw keypoints
'''
# surf = cv2.xfeatures2d.SURF_create()    # cv2.xfeatures2d.SURF_create() is not available in my environment
# kp, desc = surf.detectAndCompute(gray, None)    # ★★★★★
# surf_img = img.copy()
# cv2.drawKeypoints(gray, kp, surf_img)
# cv2.imshow('surf', surf_img)


'''
ORB, realtime detection
Create ORB object
Detect keypoints
Draw keypoints
'''
orb = cv2.ORB_create()
kp, desc = orb.detectAndCompute(gray, None)
orb_img = img.copy()
cv2.drawKeypoints(gray, kp, orb_img)
cv2.imshow('orb', orb_img)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()