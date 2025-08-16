import cv2
import numpy as np

lena = cv2.imread("B:\liond\Pictures\lena.png")
bg = np.ones(lena.shape, np.uint8)
cv2.putText(bg, "Background", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("lena", lena)
cv2.imshow("bg", bg)

add = cv2.add(lena, bg)
cv2.imshow("add", add)

sub = cv2.subtract(lena, bg)
cv2.imshow("sub", sub)

mul = cv2.multiply(lena, bg)
cv2.imshow("mul", mul)

weight = cv2.addWeighted(lena, 0.9, bg, 0.1, 0)
cv2.imshow("weight", weight)

bitwise_not = cv2.bitwise_not(lena)
cv2.imshow("bitwise_not", bitwise_not)

bitwise_and = cv2.bitwise_and(lena, bg)
cv2.imshow("bitwise_and", bitwise_and)

bitwise_or = cv2.bitwise_or(lena, bg)
cv2.imshow("bitwise_or", bitwise_or)

bitwise_xor = cv2.bitwise_xor(lena, bg)
cv2.imshow("bitwise_xor", bitwise_xor)


key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()