#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Run this file to start the app!
"""
#
# Python Ver:   3.10
#
# Author:       Tanuj Chowdhury
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 11.


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Phonebook App")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if the user clicks the upper corner,
        # "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module to keep the code clutter-free
        phonebook_gui.load_gui(self)
        
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of the window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        # defines the particular drop-down column and tearoff=0 means do not separate from menubar
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        # add_command is a child menubar item of the add_cascade parent item
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)

        self.master.config(menu=menubar, borderwidth='1')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
