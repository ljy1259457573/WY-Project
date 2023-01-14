from PIL import Image
import os,glob

def  batch_change(in_path,out_path):  #参数：输入与输出文件夹路径
    if not os.path.exists(out_path):
        print(out_path,'is not existed.')
        #创建输出文件夹
        os.mkdir(out_path)
    if not os.path.exists(in_path):
        print(in_path,'is not existed.')
        return -1
    count = 0
    for files in glob.glob(in_path+'/*'):
        filepath,filename=os.path.split(files)
        out_file = filename[0:9]+'.png' #转换成最终格式为png
        im = Image.open(files)
        new_path=os.path.join(out_path,out_file)
        print(count,',',new_path)
        count = count+1
        im.save(os.path.join(out_path,out_file))

if __name__=='__main__':
   batch_change(r'E:\WY-Project\ROI\data',r'E:\WY-Project\ROI\data') #你想转化文件所在文件夹输入和输出的路径
