from PIL import Image
import os

# 获得文件夹下所有文件
filePath = '/WY-Project/data-enhancement/data/'
filenames = os.listdir(filePath)

# 指定保存的文件夹
outputPath = '/WY-Project/data-enhancement/fan'

# 迭代所有图片
for filename in filenames:
    # 读取图像
    im = Image.open(filePath + filename)

    # 指定逆时针旋转的角度
    im_rotate = im.rotate(180)

    # 保存图像
    im_rotate.save(outputPath + filename)