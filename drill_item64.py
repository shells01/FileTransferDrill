import os
import datetime as dt
import shutil

def movefiles(source, destination):

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
    sourcefolder = 'C:/Users/Student/Desktop/FolderB'
    destfolder = 'C:/Users/Student/Desktop/FolderA'
    movefiles(sourcefolder, destfolder)

if __name__== "__main__":
    main()
                


        
