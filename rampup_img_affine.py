import cv2
import numpy as np

img = cv2.imread("lena.png")
cv2.imshow("Original", img)
h,w,c = img.shape

# 
M = np.float32([[1, 0, 100], [0, 1, 50]])
img_perspective_origin = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Affine", img_perspective_origin)

# rotate
M = cv2.getRotationMatrix2D((0, 0), 45, 1)
img_rotate = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotate", img_rotate)

src = np.float32([[0, 0], [w, 0], [0, h]])
dst = np.float32([[100, 100], [w + 100, 100], [100, h + 100]])
M = cv2.getAffineTransform(src, dst)
img_affine2 = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Affine2", img_affine2)

# perspective透视变换
img_perspective_origin = cv2.imread("affine.png")
cv2.imshow("img_perspective_origin", img_perspective_origin)
h,w,c = img_perspective_origin.shape
src = np.float32([[0, 0], [560, 128], [w, h], [0 ,h]])
dst = np.float32([[0, 0], [560, 0], [w, h], [0, h]])
M = cv2.getPerspectiveTransform(src, dst)
img_perspective = cv2.warpPerspective(img_perspective_origin, M, (w, h))
cv2.imshow("img_perspective", img_perspective)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()