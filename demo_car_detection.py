import cv2
import numpy as np
from datetime import datetime

def get_boundingRect_centerPoint(contour):
    """
    计算轮廓的边界矩形及其中心点坐标
    
    参数:
        contour: 轮廓点集，numpy数组格式
    
    返回:
        tuple: (boundingRect, center_point)
            - boundingRect: 边界矩形 (x, y, width, height)
            - center_point: 中心点坐标 (cx, cy)
    """
    boundingRect = cv2.boundingRect(contour)
    x,y,w,h = boundingRect
    cx = x + w // 2
    cy = y + h // 2

    return boundingRect, (cx, cy)

min_w = 100
min_h = 100
detection_line = 300
delta = 10

cars = []
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cap = cv2.VideoCapture('assets/car_detection.mp4')
if not cap.isOpened():
    print("Cannot open the video")

detection_line = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) * 3 // 5
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

    result = frame.copy()
    cv2.line(result, (0, detection_line), (frame.shape[1], detection_line), (0,255,0), 2)
    cv2.line(result, (0, detection_line - delta), (frame.shape[1], detection_line - delta), (255,0,0), 2)
    cv2.line(result, (0, detection_line + delta), (frame.shape[1], detection_line + delta), (255,0,0), 2)
    # find contours
    contours,h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for (i,c) in enumerate(contours):
        boundingRect, centerPoint = get_boundingRect_centerPoint(c)
        if not (boundingRect[2] > min_w and boundingRect[3] > min_h):
            continue

        cv2.rectangle(result, boundingRect, (0,0,255), 2)
        cv2.circle(result, centerPoint, delta, (255,0,0), -1)
        # print(centerPoint)
        if(detection_line - delta <= centerPoint[1] <= detection_line + delta):
            cv2.imwrite(f'B:\liond\Pictures\OpenCV_Learning\Shot-{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg',result)
            cars.append(centerPoint)

    cv2.putText(result, 'car count: ' + str(len(cars)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('origin', result)
    cv2.imshow('result', close)

    # key = cv2.waitKey(frame_time)
    key = cv2.waitKey(100)
    if(key & 0xFF ==ord('x')):
        print('exit')
        break

cap.release()
cv2.destroyAllWindows()
