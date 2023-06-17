import glob
import os

jpg_folder=r"C:\Users\Owner\Desktop\123123\TOTAL_new\images"
xml_folder=r"C:\Users\Owner\Desktop\123123\TOTAL_new\labels"

jpg_files = glob.glob(jpg_folder+'/*')
xml_files=glob.glob(xml_folder+'/*')

extention1=".jpg"
extention2='.txt'

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