#這邊可以同時更改jpg資料與標註檔(如txt,xml....)的檔名
import glob
import os

#更改資料夾位址
jpg_folder=r"C:\Users\Owner\Desktop\123123\TOTAL_new\images"
xml_folder=r"C:\Users\Owner\Desktop\123123\TOTAL_new\labels"

jpg_files = glob.glob(jpg_folder+'/*')
xml_files=glob.glob(xml_folder+'/*')

#更改附檔名名字
extention1=".jpg"
extention2='.txt'

#命名新的名字
name="testinggg"


def change_jpg(jpg_files,extention1):
    n=0
    for i in jpg_files:
        num=str(n).zfill(5)
        os.rename(i, jpg_folder + '/' + name+ num + extention1)
        n+=1
    print("jpg done")
    
def change_xml(xml_files,extention2):
    n=0
    for i in xml_files:
        num=str(n).zfill(5)
        os.rename(i, xml_folder + '/' + name + num + extention2)
        n+=1
    print("xml done")
if __name__ == '__main__':
    change_jpg(jpg_files,extention1)
    change_xml(xml_files,extention2)
