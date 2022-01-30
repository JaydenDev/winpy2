# import tkinter
from tkinter import *
import os

# create a window with title winpy2 that's 400x400 pixels
# define window
window = Tk()
window.title("winpy2")
window.geometry("400x400")

# set background color to light blue
window.configure(background='light blue')

# create a bar at the bottom of the window
bottom_bar = Frame(window)
bottom_bar.pack(side=BOTTOM)

# make a popup when START is clicked
def start_popup():
    # make exit button at top that takes full width of window
    exit_button = Button(window, text="EXIT", command=window.destroy, width=window.winfo_screenwidth())
    exit_button.pack(side=TOP)
    popup = Tk()
    popup.title("winpy2-appmenu")
    #popup.geometry("200x200")
    # position window to bottom left corner of window
    popup.geometry("+%d+%d" % (0, window.winfo_screenheight() - popup.winfo_reqheight()))
    ok_button = Button(popup, text="X", command=popup.destroy)
    ok_button.pack()
    # button labeled CALC that runs winpy2-calc.py
    calc_button = Button(popup, text="CALC", command=lambda: os.system("python winpy2-calc.py"))
    calc_button.pack()
    # button labeled SHELL that runs winpy2-shell.py
    shell_button = Button(popup, text="SHELL", command=lambda: import_shell())
    shell_button.pack()
    # button labeled EXIT that closes the window
    exit_button = Button(popup, text="EXIT", command=popup.destroy)
    exit_button.pack()
    # make button labeled shutdown that kills winpy2-shell.py
    shutdown_button = Button(popup, text="SHUTDOWN", command=lambda: os.system("pkill -f winpy2-shell.py"))
    shutdown_button.pack()
    # remove titlebar of window
    popup.overrideredirect(True)
    # make window not draggable
    popup.resizable(0,0)
    # make window not resizeable
    popup.resizable(False, False)
    # make window not moveable
    popup.grab_set()
    popup.mainloop()

# put a button on the bottom left of the bar labeled START
start_button = Button(bottom_bar, text="START", fg="green", command=start_popup)
start_button.pack(side=LEFT)
# put a button labeled "CALC" on the bottom right of the bar that runs winpy2-calc.py
calc_button = Button(bottom_bar, text="CALC", command=lambda: os.system("python winpy2-calc.py"))
calc_button.pack(side=RIGHT)
# put a button labeled "FILES" on the bottom right of the bar that runs winpy2-files.py
files_button = Button(bottom_bar, text="FILES", command=lambda: os.system("python winpy2-files.py"))
files_button.pack(side=RIGHT)
# show window
window.mainloop()