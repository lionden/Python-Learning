import cv2
import numpy as np

mouse_pos = []
def mouse_callback(event, x, y, flags, user_data):
    """
    docstring
    """
    # print(event, x, y, flags, user_data)
    global img, img6, mouse_pos
    if (event == cv2.EVENT_LBUTTONDOWN):
        mouse_pos = [(x, y)]

    elif (event == cv2.EVENT_MOUSEMOVE):
        if(flags == 1):
            mouse_pos.append((x, y))
            if(len(mouse_pos) > 1):
                cv2.polylines(img6, [np.array(mouse_pos)], False, (0,0,255), 3)

    elif (event == cv2.EVENT_RBUTTONUP):
        img6 = img.copy()

img = cv2.imread("B:\liond\Pictures\lena.png")

print(img.shape)
print(img.size)

b,g,r = cv2.split(img)
b[:,:]=255

img2 = cv2.merge((b,g,r))

cv2.imshow("Image", img)
cv2.imshow("Image2", img2)

img3 = img.copy()
cv2.line(img3, (0,0), (img.shape[1], img.shape[0]), (0,0,255), 5)
cv2.rectangle(img3, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 5)
cv2.circle(img3, (img.shape[1]//2, img.shape[0]//2), 100, (255,0,0), 5)
cv2.putText(img3, "OpenCV", (img.shape[1]//2, img.shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.imshow("Image3", img3)

# ellipse
img4 = img.copy()
cv2.ellipse(img4, (img.shape[1]//2, img.shape[0]//2), (200,100), 30, 90, 270, (255,255,255), 5)
cv2.imshow("Image4", img4)

# polyline
img5 = img.copy()
pts = np.array([(100,100), (200,100), (200,200), (100,200)])
cv2.polylines(img5, [pts], True, (255,255,255), 5)
cv2.imshow("Image5", img5)

cv2.namedWindow("Image6", cv2.WINDOW_AUTOSIZE)
img6 = img.copy()
cv2.setMouseCallback("Image6", mouse_callback, None)
while True:
    cv2.imshow("Image6", img6)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('break')
        break

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()