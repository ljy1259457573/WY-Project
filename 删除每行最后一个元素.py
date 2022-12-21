import os
filename = r"2 4 5需删除图片信息.txt"
new_filename = r"1234.txt"
with open(filename,encoding="utf-8") as f1, open(new_filename,"w",encoding="utf-8") as f2:
    for line in f1:
        new_line = line[:-4]
        f2.write(new_line)
        f2.write('\n')
f1.close()
f2.close()

