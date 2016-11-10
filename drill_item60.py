# Python course Item 60
# Drill moving files from Folder A to Folder B
import os
import shutil

source = "C:/Users/Student/Desktop/FolderA"
destination = "C:/Users/Student/Desktop/FolderB"
files = os.listdir(source)
filenames = os.listdir(destination)

# move the .txt files from Folder A to Folder B
for f in files:
    if f.endswith('.txt'):
        shutil.move(source + "/" + f, destination + "/" + f)

# print out the file paths after the files were moved
for n in filenames:
    print destination + "/" + n


