import os

files = os.listdir("E:\WY-Project\ROI\data")#原来文件夹的路径
i = 0

for file in files:
    original = "E:\WY-Project\ROI\data" + os.sep + files[i]
    #修改后放置图片的路径 F:/ns，也可将 img_ 换成其他标注
    new = "E:\WY-Project\ROI\data" + os.sep + "fan_" + str(i + 1) + ".jpg"
    os.rename(original, new)
    i += 1
