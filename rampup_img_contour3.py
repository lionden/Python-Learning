'''
min area rectangle and bounding rectangle
'''

import cv2
from rampup_img_contour import circle_points_of_contours, find_contours_via_BGR_image

def draw_lines_via_points(img:cv2.UMat, points, closed=True):
    if len(points) < 2:
        return

    for i in range(len(points) - 1):
        cv2.line(img, points[i][0], points[i+1][0], (0,255,0), 1)

    if closed:
        cv2.line(img, points[-1][0], points[0][0], (0,255,0), 1)

    pass

img = cv2.imread("assets/minArea_bounding.png")

contours = find_contours_via_BGR_image(img)
# print(contours)

minAreaRect = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(minAreaRect)
box = box.astype("int")
cv2.drawContours(img, [box], 0, (0,255,0), 1)

rect = cv2.boundingRect(contours[1])
cv2.rectangle(img, rect, (0,0,255), 1)

cv2.imshow("img", img)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()