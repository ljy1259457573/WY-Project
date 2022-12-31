# 此文件用于提取良好和欠融合

import os
import cv2

# 设置输入图像文件夹和输出 ROI 文件夹
input_folder = '/WY-Project/ROI/data/'
output_folder = '/WY-Project/ROI/'

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 读取图像
    image = cv2.imread(os.path.join(input_folder, filename))

    # 设置 ROI 的起始位置（x，y）和宽度和高度
    x, y, w, h = 390, 150, 700, 350    # 烧穿须在此处更改参数 390，150，700，350      良好与欠融合参数为200, 50, 700, 350

    # 使用 NumPy 数组切片来提取 ROI
    roi = image[y:y+h, x:x+w]

    # 使用原始文件名和输出文件夹路径构建输出文件路径
    output_path = os.path.join(output_folder, filename)

    # 保存 ROI 到新图像中
    cv2.imwrite(output_path, roi)
