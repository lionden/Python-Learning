'''
approximate and hull
'''

import cv2
from demo_img_contour import circle_points_of_contours, find_contours_via_BGR_image

def draw_lines_via_points(img:cv2.UMat, points, closed=True):
    if len(points) < 2:
        return

    for i in range(len(points) - 1):
        cv2.line(img, points[i][0], points[i+1][0], (0,255,0), 1)

    if closed:
        cv2.line(img, points[-1][0], points[0][0], (0,255,0), 1)

    pass

img = cv2.imread("assets/hand.png")

contours = find_contours_via_BGR_image(img)
# print(contours)
contour = img.copy()
cv2.drawContours(contour, contours, -1, (0,0,255), 1)
cv2.imshow("contours",contour)

#approximate
approxImg = img.copy()
approx = cv2.approxPolyDP(contours[0], 10, True)
print(approx)
draw_lines_via_points(approxImg, approx)
cv2.imshow("approx",approxImg)

#hull
hullImg = img.copy()
hull = cv2.convexHull(contours[0])
draw_lines_via_points(hullImg, hull)
cv2.imshow("hull",hullImg)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()