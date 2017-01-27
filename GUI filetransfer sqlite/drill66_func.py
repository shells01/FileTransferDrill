import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import filedialog
import os
import datetime as dt
import shutil



# Be sure to import our other modules 
# so we can have access to them
import drill66_main
import drill66_gui



def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

# ask directory command to select source/destination folders
def asksourcedir(self):
    dirname = filedialog.askdirectory()
    if dirname:
        self.source_var.set(dirname)

def askdestdir(self):
    dirname = filedialog.askdirectory()
    if dirname:
        self.dest_var.set(dirname)

# function to transfer files from source to destination
def movefiles(self):
    source = self.source_var.get()
    destination = self.dest_var.get()
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
            

# get current date and time
# create database to store date/time
# store current date/time in table
def create_db(self):
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_filecheck(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_datetime TEXT \
            );")
        # commit to save changes & close database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        #count = count_records(cur)
        cur, count = count_records(cur)
        now = dt.datetime.now()
        if count < 1:
            cur.execute("""INSERT INTO tbl_filecheck (col_datetime) VALUES (?)""",('Never'))
            conn.commit()
    conn.close()

def insert_datetime(self):
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        datetime = str(dt.datetime.now())
        cur.execute("""INSERT INTO tbl_filecheck (col_datetime) VALUES (?)""", (datetime,))
        conn.commit()
    conn.close()

# Retrieve date/time of most recent filecheck
def count_records(cur):
    conn = sqlite3.connect('db_filecheck.db')
    #with conn:
        #cur = conn.cursor()
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_filecheck""")
    count = cur.fetchone()[0]
    return cur, count
        
    conn.close()

def last_datetime(self):
    conn = sqlite3.connect('db_filecheck.db')
    with conn:
        cur = conn.cursor()
        #count = ""
        cur.execute("""SELECT col_datetime FROM tbl_filecheck ORDER BY col_datetime DESC LIMIT 1""")
        last_fc = cur.fetchone()[0]
        print(last_fc)
        self.last_fc.set(last_fc)
    conn.close()

#=========================================================



if __name__ == "__main__":
    pass
