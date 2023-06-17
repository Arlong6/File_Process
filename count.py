import xml.etree.ElementTree as ET
import shutil
import tqdm
import os

# original_path = r"D:/Github/OIDv4_ToolKit/OID/Dataset/train/Boat/Annoation_copy/"
# target_path = r"D:/Github/OIDv4_ToolKit/OID/Dataset/train/Boat/Annotation2/"
# old_classes = ["ship"]  # 需要的類別


ann_path=r"D:\Github\Pythonwork\Preprocessing\xml_process\InMRT\Annotations"

namelist=["crocs","high_heel","long_skirt","shoe"]

namelist2=["Crocs","uncertaind","Fuzzy","Rubbershoe","shoe"]

def check_file():

    crocs_count=0
    shoe_count=0
    high_heel_count=0
    long_skirt_count=0
    
    for file_name in os.listdir(ann_path):
        file_name=file_name.split('.')
        file_name=file_name[0]+".xml"
 
        ann_path_file=os.path.join(ann_path,file_name)
        
        in_file=open(ann_path_file,encoding="utf-8")
        tree=ET.parse(in_file)
        root=tree.getroot()
        for obj in root.findall('object'):
            name=str(obj.find('name').text)
            
            if name==namelist[0]:
                crocs_count+=1
            elif name==namelist[1]:
                high_heel_count+=1
            elif name==namelist[2]:
                long_skirt_count+=1
            elif name==namelist[3]:
                shoe_count+=1
    
    print("crocs number=",crocs_count)
    print("high_heel number=",high_heel_count)
    print("long_skirt number=",long_skirt_count)
    print("shoe number=",shoe_count)

def remove1():
    jpg_path=r"D:\Github\Pythonwork\Preprocessing\xml_process\InMRT\JPEGImages"
    ann_path=r"D:\Github\Pythonwork\Preprocessing\xml_process\InMRT\Annotations"
    old_classes=["uncertain","fuzzy"]
    
    name_list=[]
    c=0
    for file_name in os.listdir(ann_path):
        file_name=file_name.split('.')
        file_name=file_name[0]+".xml"
        ann_path_file=os.path.join(ann_path,file_name)
        in_file=open(ann_path_file,encoding="utf-8")
        tree=ET.parse(in_file)
        root=tree.getroot()
        for obj in root.findall('object'):
            name=str(obj.find('name').text)
            if (name in old_classes):
                name_list.append(file_name.split(".")[0])
    print(name_list)
    for file_name in os.listdir(ann_path):
        print(file_name.split(".")[0])
        if file_name.split(".")[0] in name_list:
            os.remove(file_name)        
    for file_name in os.listdir(jpg_path):
        if file_name.split(".")[0] in name_list:
            os.remove(file_name)   

    #     if file_name.split(".")[0] in name_list:
    #         os.remove(file_name)
  
                
                
                
    # print(name_list)
        # tree.write(ann_path_file)



def remove_no_ann():
    for file_name in os.listdir(ann_path):
        file_name=file_name.split('.')
        file_name=file_name[0]+".xml"
        ann_path_file=os.path.join(ann_path,file_name)
        in_file=open(ann_path_file,encoding="utf-8")
        
        tree = ET.parse(in_file)
        root = tree.getroot()
        
        print(tree)
        
       
 





def change_label():
    for file_name in os.listdir(ann_path):
        file_name=file_name.split('.')
        file_name=file_name[0]+".xml"
        ann_path_file=os.path.join(ann_path,file_name)
        in_file=open(ann_path_file,encoding="utf-8")
        tree=ET.parse(in_file)
        root=tree.getroot()
        
        for obj in root.findall('object'):
            name=str(obj.find('name').text)
            
            if name in namelist[2]:
                name = obj.find('name')
                name.text = namelist[1]
        tree.write(ann_path_file)
    print("done")





def delete_toomuch():
    ann_path=r"D:\Github\yolov5prune-5.0\Crocs-19\anno-Copy"
    crocs_count=0
    uncertain_count=0
    fuzzy_count=0
    shoe_count=0
    high_heel_count=0
    long_skirt_count=0
    c_list=[]
    for file_name in os.listdir(ann_path):
        
        a=0
        b=0        
        c=0
        d=0
        file_name=file_name.split('.')
        file_name=file_name[0]+".xml"
        ann_path_file=os.path.join(ann_path,file_name)
        in_file=open(ann_path_file,encoding="utf-8")
        tree=ET.parse(in_file)
        root=tree.getroot()
        
        for obj in root.findall('object'):
            name=str(obj.find('name').text)
            if name==namelist[0]:
                crocs_count+=1
                a+=1
            elif name==namelist[1]:
                high_heel_count+=1
                b+=1
            elif name==namelist[2]:
                long_skirt_count+=1
                d+=1
            elif name==namelist[3]:
                shoe_count+=1
                c+=1
                
        if c>5:
            c_list.append(file_name.split('.')[0])
            # print(file_name)
            

    files=os.listdir(r"D:\Github\yolov5prune-5.0\Crocs-19\train-Copy")
    k=0

    for file in files:    
        if file.split('.')[0] in c_list:

            os.remove(file)
    
    
def move_data():
    ann_path=r"D:\Data\TRAINGING_DATAS\train"
    c=0
    for file in os.listdir(ann_path):
        
        if file.endswith("xml"):
            in_file=open(file,encoding="utf-8")
            print(file)
            c+=1
    print(c)
        




if __name__ == '__main__':

    remove1()

