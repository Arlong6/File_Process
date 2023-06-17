
import os

#put jpg folder
path1 = r'C:\Users\Owner\Desktop\123123\TOTAL_new\images'

#Put xml folder
path2 = r'C:\Users\Owner\Desktop\123123\TOTAL_new\labels'

def file_name(path1,path2):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(path1):
        for file in files:
            if (os.path.splitext(file)[1] == '.jpg'):
                jpg_list.append(os.path.splitext(file)[0])


    for root, dirs, files in os.walk(path2):
        for file in files:
            if (os.path.splitext(file)[1] == '.txt'):
                xml_list.append(os.path.splitext(file)[0])


    diff = set(jpg_list).difference(set(xml_list))  # 差集，在a中但不在b中的元素
    diff2 = set(xml_list).difference(set(jpg_list))  # 差集，在b中但不在a中的元素
    
    if len(diff)>0:
        print("以下為jpg有但xml沒有")
        print("共",len(diff),"張")
        # print(len(diff))
        for name in diff:
            print( name + ".xml")
            
            
    if len(diff2)>0:
        print("以下為xml有但jpg沒有")
        print("共",len(diff2),"張")
        for name in diff2:
            print( name + ".jpg")
            
    
    if len(diff) == len (diff2) ==  0:
        print("Clear!")


    # ann_path=os.listdir(r'D:\Github\yolov5prune-5.0\Crocs-19\anno-Copy')
    # files2=[]
    # for files in ann_path:
    #     if files.split('.')[0] in diff2:
    #         files2.append(files)
    #         os.remove(files)
            
    # print(len(files2))
    
if __name__ == '__main__':

    file_name(path1,path2)