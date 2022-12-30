import cv2
import numpy as np
import os.path
import copy

# 椒盐噪声
def SaltAndPepper(src, percetage):
    SP_NoiseImg = src.copy()
    SP_NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(SP_NoiseNum):
        randR = np.random.randint(0, src.shape[0] - 1)
        randG = np.random.randint(0, src.shape[1] - 1)
        randB = np.random.randint(0, 3)
        if np.random.randint(0, 1) == 0:
            SP_NoiseImg[randR, randG, randB] = 0
        else:
            SP_NoiseImg[randR, randG, randB] = 255
    return SP_NoiseImg

# 高斯噪声
def addGaussianNoise(image, percetage):
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum = int(percetage * image.shape[0] * image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0, h)
        temp_y = np.random.randint(0, w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg


# 图片文件夹路径
file_dir = r'E:\WY-Project\data-enhancement\data/'
for img_name in os.listdir(file_dir):
    img_path = file_dir + img_name
    img = cv2.imread(img_path)

    # 增加噪声
    # img_salt = SaltAndPepper(img, 0.3)
    # cv2.imwrite(file_dir + img_name[0:7] + '_salt.jpg', img_salt)
    img_gauss = addGaussianNoise(img, 0.3)
    cv2.imwrite(file_dir + img_name[0:-4] + '_noise.jpg', img_gauss)

