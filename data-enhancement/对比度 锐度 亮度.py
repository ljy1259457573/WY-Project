from PIL import Image
from PIL import ImageEnhance
import os

rootdir = r'/WY-Project/data-enhancement/data'  # 指明被遍历的文件夹
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        currentPath = os.path.join(parent, filename)
        im = Image.open(currentPath)
        print(filename)

        # 增加对比度
        enh_con = ImageEnhance.Contrast(im)
        image_contrasted = enh_con.enhance(0.5)
        newname1 = r"/WY-Project/data-enhancement/data/vl-duib" + filename
        image_contrasted.save(newname1)

        # 增加锐度
        enh_sha = ImageEnhance.Sharpness(im)
        image_sharped = enh_sha.enhance(3.0)
        newname2 = r"/WY-Project/data-enhancement/data/vl-rui" + filename
        image_sharped.save(newname2)

        # 增加亮度
        enh_bri = ImageEnhance.Brightness(im)
        image_brightened = enh_bri.enhance(1.2)
        newname3 = r"/WY-Project/data-enhancement/data/vl-brig" + filename
        image_brightened.save(newname3)
