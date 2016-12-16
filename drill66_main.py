# Python 3.5(32 bit)
# Drill Item 66
# Main file
# Shelly Ahn
# Tested OS: Windows 7

from tkinter import *
import tkinter as tk
import sqlite3
import datetime as dt
import os
import shutil

# Import other modules
import drill66_func
import drill66_gui

# Frame is the Tkinter frame class that our own class will inherit from
# ParentWindow class

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

         # define our master frame configuration
        self.master = master
        self.master.minsize(500,400) #(Height, Width)
        self.master.maxsize(500,400)
        # This CenterWindow method will center our app on the user's screen
        drill66_func.center_window(self,500,500)
        self.master.title("File Transfer Project")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: drill66_func.ask_quit(self))
        arg = self.master
        # string variable
        self.last_fc = StringVar()

# load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        drill66_gui.load_gui(self)
        drill66_func.create_db(self)
        drill66_func.first_run(self)
        drill66_func.last_datetime(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
