import cv2

img = cv2.imread('B:\liond\Pictures\软件工程师.jpg')

cv2.namedWindow('image',cv2.WINDOW_NORMAL)


while True:
    cv2.imshow('image',img)

    key=cv2.waitKey(0)
    print(key)
    if(key & 0xFF ==ord('q')):
        print('exit')
        break
    elif(key & 0xFF ==ord('s')):
        # cv2.addText('hello world',img)
        cv2.imwrite('B:\liond\Pictures\软件工程师_new.jpg',img)

cv2.destroyAllWindows()
