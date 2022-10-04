#import packages
import tkinter as tk
from tkinter import *
import LogicpdfSearch

#create window
window = Tk()

def fetchEntry():
    #fetch input, call pdf search and close window
    entry = entry_box1.get()
    input_path = entry_box2.get()
    chosen_name = entry_box3.get()
    output_path = entry_box4.get()
    global Targetlist
    Targetlist = entry.split()
    LogicpdfSearch.textSearch(input_path, Targetlist, chosen_name, output_path)
    window.destroy()

def startup():
    #add window elements and open window
    label1=tk.Label (text= "Insert target words seperated by a blank space")
    label2=tk.Label (text= "Insert file path")
    label3=tk.Label (text= "Insert output file name")
    label4=tk.Label (text= "Insert output directory path and press OK")
    global entry_box1
    global entry_box2
    global entry_box3
    global entry_box4
    entry_box1 = tk.Entry()
    entry_box2 = tk.Entry()
    entry_box3 = tk.Entry()
    entry_box4 = tk.Entry()
    label1.pack()
    entry_box1.pack()
    label2.pack()
    entry_box2.pack()
    label3.pack()
    entry_box3.pack()
    label4.pack()
    entry_box4.pack()
    B = Button(text="OK", command=fetchEntry)
    B.pack()
    window.mainloop()

startup()