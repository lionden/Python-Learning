import cv2
import numpy as np

def get_homography(img1, img2):
    """
    计算两幅图像之间的单应性变换矩阵
    
    该函数使用SIFT特征检测和匹配来找到两幅图像之间的对应点，
    然后使用RANSAC算法计算单应性变换矩阵
    
    参数:
        img1: 第一幅输入图像
        img2: 第二幅输入图像
    
    返回值:
        H: 3x3的单应性变换矩阵，如果匹配点不足则返回None
    """
    # 创建特征转换对象
    # 通过特征转换对象获得特征点和描述子
    # 创建特征匹配器
    # 过滤特征, 找出有效的特征匹配点
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)  # 选取最优的两个进行匹配
    print(matches)

    good = []
    for m1, m2 in matches:
        if m1.distance < 0.8 * m2.distance:
            good.append(m1)

    if len(good) >= 8:
        # img1Pts = []
        # img2Pts = []
        # for m in good:
        #     img1Pts.append(kp1[m.queryIdx].pt)
        #     img2Pts.append(kp2[m.trainIdx].pt)

        # # [(x1, y1), (x2, y2), ...] -> [[x1, y1], [x2, y2], ...]
        # img1Pts = np.float32(img1Pts).reshape(-1, 1, 2)
        # img2Pts = np.float32(img2Pts).reshape(-1, 1, 2)
        # The following line is equivalent to the above two lines

        img1Pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        img2Pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        H, _ = cv2.findHomography(img1Pts, img2Pts, cv2.RANSAC, 5.0)
        
        return H
    
    else:
        print("Not enough matches are found - {}/{}".format(len(good), 8))
        return None


def warp_image(img1, img2, H):
    """
    将图片进行变换
    
    参数:
        img1: 输入图片
        img2: 输入图片
        H: 单应性矩阵
    
    返回值:
        img_warp: 变换后的图片
    """
    # 获得每张图片的角点
    # 对图片进行变化: 通过单应性矩阵进行旋转, 平移
    # 创建一张大图, 将变换后的图片和另一张图片融合在一起
    # 将结果输出
    h1, w1, _ = img1.shape
    h2, w2, _ = img2.shape
    img1Corners = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2Corners = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)

    img1_transform = cv2.perspectiveTransform(img1Corners, H)
    
    print(img1Corners)
    print(img2Corners)
    print(img1_transform)

    result_dims = np.concatenate((img2Corners, img1_transform), axis=0) # axis=0表示按行连接(横向), axis=1表示按列连接
    print(result_dims)

    [xmin, ymin] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    print(xmin, ymin, xmax, ymax)

    # 构建齐次变换矩阵
    transform_array = np.array([[1, 0, abs(xmin)],
                                [0, 1, abs(ymin)],
                                [0, 0, 1]])
    result_img = cv2.warpPerspective(img1, transform_array.dot(H), (xmax - xmin, ymax - ymin))
    result_img[abs(ymin):h2 + abs(ymin), abs(xmin):w2 + abs(xmin)] = img2

    return result_img


# 图像拼接步骤
# 1. 读取图片, 并将图片设置为同样大小
# 2. 找特征点, 描述子, 计算单应性矩阵
# 3. 根据单应性矩阵对图像进行变换, 然后平移
# 4. 融合图像并输出显示

img_left = cv2.imread('assets/panorama_left.png')
img_right = cv2.imread('assets/panorama_right.png')

print(img_left.shape)
h, w, _ = img_left.shape
img_right = cv2.resize(img_right, (w, h))

# 将左右水平拼接
inputs = np.hstack((img_left, img_right))
cv2.imshow('inputs', inputs)

H = get_homography(img_left, img_right)
img_warp = warp_image(img_left, img_right, H)
cv2.imshow('img_warp', img_warp)

key = cv2.waitKey(0)
if(key & 0xFF ==ord('x')):
    print('exit')
    exit()

cv2.destroyAllWindows()