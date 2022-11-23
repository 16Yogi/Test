from tkinter import *

win = Tk()

name = Label(win,text="Name").place(x=30,y=50)
email = Label(win,text="Email").place(x=30,y=90)
password = Label(win,text="password").place(x=30,y=130)

e1 = Entry(win).place(x=90,y=50)
e2 = Entry(win).place(x=90,y=90)
e3 = Entry(win).place(x=100,y=130)

win.mainloop()