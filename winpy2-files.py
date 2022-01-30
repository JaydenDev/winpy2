# import tkinter
from tkinter import *
import os

# make window
window = Tk()
window.title("winpy2")
window.geometry("400x400")

# list files in directory and set result to variable
dir_list = os.listdir()

# make a label for the variable and put it in the window
label = Label(window, text=dir_list)
label.pack()

# remove titlebar of window
window.overrideredirect(True)
# make window not draggable
window.resizable(0, 0)
# make window not resizeable
window.resizable(False, False)
# make window not moveable
window.grab_set()

# show window
window.mainloop()
