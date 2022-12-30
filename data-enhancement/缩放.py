# import os
# import cv2
#
# DATADIR="E:\WY-Project\data-enhancement\data"
# IMG_SIZE=300
#
# path=os.path.join(DATADIR)
# img_list=os.listdir(path)
# ind=0
# for i in img_list:
#     img_array=cv2.imread(os.path.join(path,i),cv2.IMREAD_COLOR)
#     new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
#     img_name=str(ind)+'.png'
#     save_path='E:\\WY-Project\\data-enhancement\\'+str(ind)+'.png'
#     ind=ind+1
#     cv2.imwrite(save_path,new_array)


# 该文件需和图片放在同一路径下
import os
from PIL import Image
# 遍历文件夹中的所有文件
for file in os.listdir("."):
    # 只处理 png 文件
    if file.endswith(".png"):
        # 打开文件
        im = Image.open(file)
        # 缩放到50%
        im_resized = im.resize((int(im.size[0] * 0.5), int(im.size[1] * 0.5)))
        # 保存缩放后的图片
        im_resized.save("resized_" + file)

