import cv2
import numpy as np

# 获取图片
image = cv2.imread('lianghao.png', cv2.IMREAD_UNCHANGED)

# 定义一个300*300的矩阵 3为通道数
strawberry = np.ones((700, 350, 3))

# 原始图片
cv2.imshow("demo", image)

# ROI区域
strawberry = image[50:400, 200:900]

cv2.imshow("berries", strawberry)

cv2.imwrite('lll.png', strawberry)

cv2.waitKey(0)
cv2.destroyAllWindows()