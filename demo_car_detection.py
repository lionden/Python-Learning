import cv2
from matplotlib import contour
import numpy as np
import datetime

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
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
    # remove background
    mask = bgsubmog.apply(blur)

    # erode and dilate, can be used to remove noise on the background
    erode = cv2.erode(mask, kernal)
    dilate = cv2.dilate(erode, kernal)

    # Morphology close: can be used to remove noise inside the object
    close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernal)

    # find contours
    contours,h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for (i,c) in enumerate(contours):
        boundingRect = cv2.boundingRect(c)
        cv2.rectangle(frame, boundingRect, (0,0,255), 2)

    cv2.imshow('origin', frame)
    cv2.imshow('result', close)

    key = cv2.waitKey(frame_time)
    if(key & 0xFF ==ord('x')):
        print('exit')
        break

cap.release()
cv2.destroyAllWindows()
