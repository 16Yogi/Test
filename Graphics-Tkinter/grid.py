from tkinter import *

win = Tk()

name = Label(win,text="Name").grid(row=0,column=0)
e1 = Entry(win).grid(row=0,column=1)
password = Label(win,text="Password").grid(row=1,column=0)
e3 = Entry(win).grid(row=1,column=1)
submit= Button(win,text="Submit",fg="blue").grid(row=8,column=10)

win.mainloop()
