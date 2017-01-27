# Python 3.5(32 bit)
# Drill Item 65
# UI with File Transfer Project
# GUI file
# Shelly Ahn
# Tested OS: Windows 7

from tkinter import *
import tkinter as tk


# Import the other modules
import GUI_filetransfer_func
import GUI_filetransfer_main


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
    """
    # labels that display source and destination folders
    self.lbl_source = tk.Label(self.master,text='Source Folder')
    self.lbl_source.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_dest = tk.Label(self.master,text='Destination Folder')
    self.lbl_dest.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.source_var = StringVar()
    self.txt_source = tk.Entry(self.master, textvariable = self.source_var)
    self.txt_source.grid(row=1,column=0,rowspan=1,
                         columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.dest_var = StringVar()
    self.txt_dest = tk.Entry(self.master, textvariable = self.dest_var)
    self.txt_dest.grid(row=3,column=0,rowspan=1,
                       columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)
   
    # buttons to select source and destination folders
    
    self.btn_source = tk.Button(self.master,width=24,height=1,
                             text='Select source folder',
                             command=lambda: GUI_filetransfer_func.asksourcedir(self))
    self.btn_source.grid(row=0,column=3,columnspan = 2,
                      padx=(10,0),pady=(25,10),sticky=W)
    self.btn_dest = tk.Button(self.master,width=24,height=1,
                                text='Select destination folder',
                                command=lambda: GUI_filetransfer_func.askdestdir(self))
    self.btn_dest.grid(row=2,column=3,columnspan = 2,
                         padx=(10,0),pady=(25,10),sticky=E)
    
    # Button to transfer files from source folder to destination folder
    self.btn_move = tk.Button(self.master, width=24, height=2,
                              text='Transfer files',
                              command=lambda: GUI_filetransfer_func.movefiles(self))
    self.btn_move.grid(row=5, column=2, columnspan = 3, padx =(10,0), pady=(25,10),sticky=S)
    

    

    



if __name__ == "__main__":
    pass

