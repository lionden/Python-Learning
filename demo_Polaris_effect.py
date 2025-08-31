from email.mime import image
import cv2
from matplotlib.pyplot import cla
import numpy as np
from datetime import datetime

# cap = cv2.VideoCapture('D:\\tmp\\Tommy\\input.mp4')
cap = cv2.VideoCapture('D:\\tmp\\Tommy\\fc9ed7c9-76fe-4509-96e5-11ceeb280420.mov')
if not cap.isOpened():
    print("Cannot open the video")

print(cap.get(cv2.CAP_PROP_FPS))
frame_time = int(1000 / cap.get(cv2.CAP_PROP_FPS))
print(frame_time)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read the video")
        break

    cv2.imshow('origin', frame)
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # cv2.imshow('origin2', image)

    lab = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    lab = cv2.merge((cl,a,b))

    image = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    # cv2.imshow('CLAHE', image)

    # 3. HSV空间调整色相/饱和度/亮度（Polaris核心步骤）
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV).astype(np.float32)

    # 提升蓝青色的饱和度（hue约90~150）
    mask_blue_cyan = ((hsv[:,:,0] >= 90) & (hsv[:,:,0] <= 150))
    hsv[:,:,1][mask_blue_cyan] *= 1.3

    # 压低红色/黄色的饱和度与亮度（hue约0~30和150~180）
    mask_red = ((hsv[:,:,0] <= 20) | (hsv[:,:,0] >= 170))
    mask_yellow = ((hsv[:,:,0] >= 20) & (hsv[:,:,0] <= 40))
    hsv[:,:,1][mask_red | mask_yellow] *= 0.7
    hsv[:,:,2][mask_red | mask_yellow] *= 0.9

    # 防止数值溢出
    hsv[:,:,1] = np.clip(hsv[:,:,1], 0, 255)
    hsv[:,:,2] = np.clip(hsv[:,:,2], 0, 255)

    image = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)

    # 4. 增加整体冷色倾向（可选：加偏色）
    blue_tint = np.zeros_like(image)
    blue_tint[:,:,2] = 30  # 适量提升蓝色通道
    result = cv2.addWeighted(image, 0.9, blue_tint, 0.1, 0)

    # 5. 保存/显示结果
    # cv2.imwrite('output.jpg', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    cv2.imshow('Polaris Effect', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))



    # key = cv2.waitKey(frame_time)
    key = cv2.waitKey(100)
    if(key & 0xFF ==ord('x')):
        print('exit')
        break

cap.release()
cv2.destroyAllWindows()
