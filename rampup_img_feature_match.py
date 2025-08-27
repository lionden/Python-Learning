import cv2
import numpy as np

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
result = cv2.drawMatches(img, kp, img_beitie, kp_beitie, matches, None)
cv2.imshow('result',result)




key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()