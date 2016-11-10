# Python course Item 60
# Drill moving files from Folder A to Folder B
import os
import shutil

shutil.move("C:/Users/Student/Desktop/FolderA/file1.txt", "C:/Users/Student/Desktop/FolderB/file1.txt")
shutil.move("C:/Users/Student/Desktop/FolderA/file2.txt", "C:/Users/Student/Desktop/FolderB/file2.txt")
shutil.move("C:/Users/Student/Desktop/FolderA/file3.txt", "C:/Users/Student/Desktop/FolderB/file3.txt")
shutil.move("C:/Users/Student/Desktop/FolderA/file4.txt", "C:/Users/Student/Desktop/FolderB/file4.txt")

directory = "C:/Users/Student/Desktop/FolderB"
filenames = os.listdir(directory)

for f in filenames:
    print directory + "/" + f



