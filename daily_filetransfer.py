# Shelly Ahn
# Python Course
# Daily File Transfer
# Python 2.7
# Tested on Windows 7
"""
Scenario:
Your company's users create or edit a collection of text files throughout the day.
Once a day, files that are new, or edited within 24 hours,
are sent to a destination folder on the computer, then sent to the home office.

Task:
- Create 2 folders, 1 for the source files & 1 to be the destination folder.
- Create a script that will automate this daily file transfer process. 
"""

import os
import datetime as dt
import shutil

# define the movefiles function
def movefiles(source, destination):

    # define the variables now (current time) and ago (24 hours ago from now)
    now = dt.datetime.now()
    ago = now - dt.timedelta(hours=24)

    # Check and print which files were updated/created within past 24 hours
    # Transfer the files from 1 folder to another
    for root, dirs, files in os.walk(source):
        for f in files:
            filename = os.path.join(root, f)
            st = os.stat(filename)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                shutil.move(filename, destination)

# main function
def main():
    sourcefolder = 'C:/Users/Student/Desktop/FolderA'
    destfolder = 'C:/Users/Student/Desktop/FolderB'
    movefiles(sourcefolder, destfolder)

if __name__== "__main__":
    main()
                


        
