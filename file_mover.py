# Shelly Ahn
# Python course, the Tech Academy
# File Mover drill
# Python 2.7
# Tested on Windows 7
"""
Scenario:
Your employer wants a program to move all his .txt files
from folder A to folder B with one click.
Create 2 folders on your desktops: Folder A and Folder B
Create 4 random .txt files & put them in Folder A.

Task:
-Move the files from Folder A to Folder B
-Print out each file path that got moved to Folder B
"""
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

