# Python 3.5(32 bit)
# Drill Item 66
# GUI file
# Shelly Ahn
# Tested OS: Windows 7

from tkinter import *
import tkinter as tk
import sqlite3
import datetime as dt
import os
import shutil


# Import the other modules
import drill66_func
import drill66_main


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        Use the grid geometry manager
    """
    # labels that display source and destination folders
    self.lbl_source = tk.Label(self.master,text='Source Folder')
    self.lbl_source.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky=N+W)
    self.lbl_dest = tk.Label(self.master,text='Destination Folder')
    self.lbl_dest.grid(row=2,column=0,padx=(10,0),pady=(10,0),sticky=N+W)

    self.source_var = StringVar()
    self.txt_source = tk.Entry(self.master, textvariable = self.source_var)
    self.txt_source.grid(row=1,column=0,rowspan=1,
                         columnspan=3,padx=(10,40),pady=(0,0),sticky=N+E+W)
    self.dest_var = StringVar()
    self.txt_dest = tk.Entry(self.master, textvariable = self.dest_var)
    self.txt_dest.grid(row=3,column=0,rowspan=1,
                       columnspan=3,padx=(10,40),pady=(0,0),sticky=N+E+W)
   
    # buttons to select source and destination folders
    
    self.btn_source = tk.Button(self.master,width=24,height=1,
                             text='Select source folder',
                             command=lambda: drill66_func.asksourcedir(self))
    self.btn_source.grid(row=0,column=3,rowspan = 2, columnspan = 3,
                      padx=(10,0),pady=(10,10),sticky=E)
    self.btn_dest = tk.Button(self.master,width=24,height=1,
                                text='Select destination folder',
                                command=lambda: drill66_func.askdestdir(self))
    self.btn_dest.grid(row=2,column=3,rowspan = 2, columnspan = 3,
                         padx=(10,0),pady=(10,10),sticky=E)
    
    # Button to transfer files from source folder to destination folder
    self.btn_move = tk.Button(self.master, width=24, height=2,
                              text='Transfer files',
                              command=lambda: drill66_func.movefiles(self))
    self.btn_move.grid(row=5, column=2, columnspan = 3, padx =(10,0), pady=(25,10),sticky=S)

    # Label to display date/time of most recent filecheck
    
    self.lbl_filecheck = tk.Label(self.master,
                                  text = "Most recent filecheck: ")
    self.lbl_filecheck.grid(row=7, column=3, padx=(25,0), pady=(10,0))
    #self.txt_filecheck = StringVar()
    self.txt_filecheck = tk.Label(self.master, textvariable = self.last_fc)
    self.txt_filecheck.grid(row=9, column=1, columnspan = 7, padx = (10,0), pady=(25,10))

    
    

    

    



if __name__ == "__main__":
    pass

