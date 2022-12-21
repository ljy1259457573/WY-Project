import os

# 读取 txt 文件中的图片路径
with open('1.txt', 'r') as f:
    paths = f.readlines()

# 遍历图片路径列表，并删除图片
for path in paths:
    path = path.strip()  # 删除路径中的换行符
    if os.path.exists(path):  # 判断图片是否存在
        os.remove(path)  # 删除图片
    else:
        print(f'{path} no exist')
