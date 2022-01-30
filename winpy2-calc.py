# import tkinter
from tkinter import *

# make a calculator window
window = Tk()
window.title("winpy2-calc")
window.geometry("400x400")

# set background color to light blue
window.configure(background='light blue')

# make exit button at top that takes full width of window
exit_button = Button(window, text="EXIT", command=window.destroy, width=window.winfo_screenwidth())
exit_button.pack(side=TOP)

# make label for math functions
label = Label(window, text="", font=("Arial Bold", 20))
label.pack()

# remove titlebar of window
window.overrideredirect(True)
# make window not draggable
window.resizable(0, 0)
# make window not resizeable
window.resizable(False, False)
# make window not moveable
window.grab_set()

# make math functions


def add(x, y):
    return x + y
# make subtract function


def subtract(x, y):
    return x - y
# make multiply function


def multiply(x, y):
    return x * y
# make divide function


def divide(x, y):
    return x / y
# make clear function


def clear():
    x.delete(0, END)
    y.delete(0, END)


# make calculator buttons
# define buttons that do math functions
button_1 = Button(window, text="1", padx=40, pady=20,
                  command=lambda: x.insert(END, "1"))
button_2 = Button(window, text="2", padx=40, pady=20,
                  command=lambda: x.insert(END, "2"))
button_3 = Button(window, text="3", padx=40, pady=20,
                  command=lambda: x.insert(END, "3"))
button_4 = Button(window, text="4", padx=40, pady=20,
                  command=lambda: x.insert(END, "4"))
button_5 = Button(window, text="5", padx=40, pady=20,
                  command=lambda: x.insert(END, "5"))
button_6 = Button(window, text="6", padx=40, pady=20,
                  command=lambda: x.insert(END, "6"))
button_7 = Button(window, text="7", padx=40, pady=20,
                  command=lambda: x.insert(END, "7"))
button_8 = Button(window, text="8", padx=40, pady=20,
                  command=lambda: x.insert(END, "8"))
button_9 = Button(window, text="9", padx=40, pady=20,
                  command=lambda: x.insert(END, "9"))
button_0 = Button(window, text="0", padx=40, pady=20,
                  command=lambda: x.insert(END, "0"))
button_add = Button(window, text="+", padx=40, pady=20,
                    command=lambda: x.insert(END, "+"))
button_subtract = Button(window, text="-", padx=40,
                         pady=20, command=lambda: x.insert(END, "-"))
button_multiply = Button(window, text="*", padx=40,
                         pady=20, command=lambda: x.insert(END, "*"))
button_divide = Button(window, text="/", padx=40, pady=20,
                       command=lambda: x.insert(END, "/"))
button_equal = Button(window, text="=", padx=40, pady=20,
                      command=lambda: y.insert(END, eval(x.get())))
button_clear = Button(window, text="C", padx=40, pady=20, command=clear)

# pack buttons
button_1.pack(side=TOP, fill=BOTH, expand=True)
button_2.pack(side=TOP, fill=BOTH, expand=True)
button_3.pack(side=TOP, fill=BOTH, expand=True)
button_4.pack(side=TOP, fill=BOTH, expand=True)
button_5.pack(side=TOP, fill=BOTH, expand=True)
button_6.pack(side=TOP, fill=BOTH, expand=True)
button_7.pack(side=TOP, fill=BOTH, expand=True)
button_8.pack(side=TOP, fill=BOTH, expand=True)
button_9.pack(side=TOP, fill=BOTH, expand=True)
button_0.pack(side=TOP, fill=BOTH, expand=True)
button_add.pack(side=TOP, fill=BOTH, expand=True)
button_subtract.pack(side=TOP, fill=BOTH, expand=True)
button_multiply.pack(side=TOP, fill=BOTH, expand=True)
button_divide.pack(side=TOP, fill=BOTH, expand=True)
button_equal.pack(side=TOP, fill=BOTH, expand=True)
button_clear.pack(side=TOP, fill=BOTH, expand=True)

# show window
window.mainloop()
