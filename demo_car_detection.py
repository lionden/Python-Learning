import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture('assets/car_detection.mp4')
if not cap.isOpened():
    print("Cannot open the video")

print(cap.get(cv2.CAP_PROP_FPS))
frame_time = int(1000 / cap.get(cv2.CAP_PROP_FPS))
print(frame_time)
bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read the video")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    mask = bgsubmog.apply(blur)

    cv2.imshow('origin', frame)
    cv2.imshow('mask', mask)

    key = cv2.waitKey(frame_time)
    if(key & 0xFF ==ord('x')):
        print('exit')
        break

cap.release()
cv2.destroyAllWindows()
