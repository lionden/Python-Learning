import cv2
import numpy as np

img = cv2.imread('lena.jpg')


key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()