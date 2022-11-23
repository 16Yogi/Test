from tkinter import *

win = Tk()

button = Button(win, text="first",fg="red")
button.pack(side=TOP)
button = Button(win, text="second",fg="blue")
button.pack(side=LEFT)
button = Button(win, text="third", fg="green")
button.pack(side=RIGHT)
button = Button(win, text="fourth",fg="blue")
button.pack(side=BOTTOM)

win.mainloop()

