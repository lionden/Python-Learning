import cv2

img = cv2.imread("assets/contour.png")
cv2.imshow("img",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("binary",binary)

contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
cv2.drawContours(img, contours, -1, (0,0,255), 1)

for contour in contours:
    print(contour)
    print(f'Area: {cv2.contourArea(contour)}, Length: {cv2.arcLength(contour, True)}')
    print('----------------------')
    # cv2.putText(img, f"Area: {cv2.contourArea(contour)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    for point in contour:
        print(point)
        cv2.circle(img, (point[0][0], point[0][1]), 5, (0,255,0), 3)

cv2.imshow("contours",img)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()