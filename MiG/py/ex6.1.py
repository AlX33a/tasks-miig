import zipfile
import os
from datetime import datetime
import codecs
import shutil
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("namez")
parser.add_argument("namef")
namespace = parser.parse_args()

lines = 0
letters = 0
filename = 'sample.zip'

with zipfile.ZipFile(filename) as zip:
    ziplist = zip.namelist()
    print(zip.namelist())

with zipfile.ZipFile(filename,'r') as zfile:
    zfile.extractall()
open('01.txt', 'w').close()

zip.close()

file = open("03.txt", "w")
file.close()

with codecs.open( '02.txt', "r", "utf_8_sig" ) as file:
    for line in codecs.open( '02.txt', "r", "utf_8_sig" ):
        lines += 1
        letters += len(line)

file = open("02.txt", "w").close()
file = open("02.txt", "w+")
file.write(f"{ziplist}\n Letters: {letters}")
file.close()

file = codecs.open( f'{namespace.namef}.txt', "+w", "utf_8_sig" )
file.write(f"Выполнил Пелых Александр Святославович \nГруппа ИСиТ 1-1Б \n{str(datetime.now())[:-7]}")
file.close()

source_path1 = "01.txt"
source_path2 = "02.txt"
source_path3 = "03.txt"
os.mkdir("path")
shutil.move(source_path1, 'path')
shutil.move(source_path2, 'path')
shutil.move(source_path3, 'path')

shutil.make_archive(f"{namespace.namez}", "zip", "path")
shutil.rmtree('path')