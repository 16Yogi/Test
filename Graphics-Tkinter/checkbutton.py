from tkinter import *

win = Tk()

win.geometry('500x500')
win.title('CheckButton')

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

# lit = Label(text="THis is list of fruits?DO you like any fruits")


l1 = Label(text="What is your Faivare Fruits-").grid(row=0,column=0)
cb1 = Checkbutton(text="Mango",variable=checkvar1,onvalue=1,offvalue=0).grid(row=2,column=2)
cb2 = Checkbutton(text="Banana",variable=checkvar2,onvalue=1,offvalue=0).grid(row=3,column=2)
cb3 = Checkbutton(text="Orange",variable=checkvar3,onvalue=1,offvalue=0).grid(row=4,column=2)

win.mainloop()