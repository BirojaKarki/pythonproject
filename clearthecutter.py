'''
Write a program to clear the cutter inside a folder on your computer.You should os module to renmae all the png images
from 1.png all the way till n.png where n is the number of png files in that folder >Do thr same for other file formats


'''
import os

#os.mkdir("folder")#to make folder
files=os.listdir("folder")
i=1
for file in files:
  if file.endswith(".JPG"):
    print(file)
    os.rename(f"folder/{file}",f"folder/{i}.png")
    i=i+1