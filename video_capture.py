from datetime import datetime
import cv2
import numpy as np

def mouse_callback(event, x, y, flags, user_data):
    """
    鼠标回调函数，用于处理鼠标事件
    
    参数:
        event: 鼠标事件类型
        x: 鼠标点击位置的x坐标
        y: 鼠标点击位置的y坐标
        flags: 鼠标事件标志位
        user_data: 用户自定义数据
    
    返回值:
        无
    """
    # 打印鼠标事件的相关信息
    print(event, x, y, flags, user_data)


cv2.namedWindow("Capture", cv2.WINDOW_NORMAL)

i=1
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter(f'B:\liond\Pictures\OpenCV_Learning\Record-{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi',fourcc,25, (640,480)) # (1920,1080))
cv2.setMouseCallback("Capture", mouse_callback, "from cv2 camera capture")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frm = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Capture", np.zeros_like(frm))
    vw.write(frm)

    key=cv2.waitKey(40)
    if(key & 0xFF ==ord('q')):
        print('exit')
        break
    elif(key & 0xFF ==ord('c')):
        # cv2.addText('hello world',img)
        cv2.imwrite(f'B:\liond\Pictures\OpenCV_Learning\Shot-{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg',frm)

cap.release()
vw.release()
cv2.destroyAllWindows()
