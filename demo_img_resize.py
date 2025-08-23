import cv2
import numpy as np

img = cv2.imread("B:\liond\Pictures\lena.png")

# resize
y,x,c=img.shape
img_resize = cv2.resize(img, ((int)(x * 0.5), (int)(y * 0.5)))
img_resize2 = cv2.resize(img, None, fx=1.2, fy=1.2)

cv2.imshow("img", img)
cv2.imshow("img_resize", img_resize)
cv2.imshow("img_resize2", img_resize2)

# flip
img_flip0 = cv2.flip(img, 0)
img_flip1 = cv2.flip(img, 1)
img_flip = cv2.flip(img, -1)
cv2.imshow("img_flip 0", img_flip0)
cv2.imshow("img_flip 1", img_flip1)
cv2.imshow("img_flip -1", img_flip)


# rotate
img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("img_rotate", img_rotate)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()