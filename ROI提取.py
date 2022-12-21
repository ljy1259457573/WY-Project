import cv2
def on_mouse(event, x, y, flags, param):
    global img, click, slip    #定义局部变量全局可用
    img2 = img.copy()          #将原图复制copy一份给我处理
    if event == cv2.EVENT_LBUTTONDOWN:   #库函数————左键点击
        click = (x,y)             #定义一个参数存放点击的坐标
        cv2.circle(img2, click, 5, (255,255,0), 5)  #点的时候显示一个小点即圆点供用户交互
        cv2.imshow('pic', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):   #鼠标按住左键拖曳
        cv2.rectangle(img2, click, (x,y), (0,125,255), 5)#上一步记录的坐标点作为起点，用户拖拽轨迹点为终点画矩形框
        cv2.imshow('pic', img2)
    elif event == cv2.EVENT_LBUTTONUP:  #当鼠标左键释放时
        slip = (x,y)
        cv2.rectangle(img2, click, slip, (0,0,255), 5)
        cv2.imshow('pic', img2)
        min_x = min(click[0],slip[0])
        min_y = min(click[1],slip[1])
        width = abs(click[0] - slip[0])
        height = abs(click[1] -slip[1])
        roi = img[min_y:min_y+height, min_x:min_x+width]#提取此时的ROI区域
        cv2.destroyAllWindows()
        cv2.imshow('ROI', roi)

img = cv2.imread('qianronghe.png')
print("--------- HL截取ROI区域的测试 ---------")
cv2.namedWindow('pic')
cv2.setMouseCallback('pic', on_mouse)
cv2.imshow('pic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#保存图片
cv2.imwrite('qianronghe.png', img)
