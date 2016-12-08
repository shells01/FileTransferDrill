# Python 3.5(32 bit)
# Drill Item 65
# UI for File Transfer Project
# Main file
# Shelly Ahn
# Tested OS: Windows 7

from tkinter import *
import tkinter as tk

# Import other modules
import GUI_filetransfer_func
import GUI_filetransfer_gui

# Frame is the Tkinter frame class that our own class will inherit from
# ParentWindow class

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

         # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        GUI_filetransfer_func.center_window(self,500,300)
        self.master.title("GUI for File Transfer Project")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: GUI_filetransfer_func.ask_quit(self))
        arg = self.master

# load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        GUI_filetransfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
