from tkinter import *

win = Tk()
win.geometry('500x500')
win.title('Entry')

l1 = Label(text="Name:",bg="blue").grid(row=0,column=0)
e1 = Entry(text='Enter your Name').grid(row=0,column=4)

l2 = Label(text="mothers name").grid(row=1,column=0)
e2 = Entry(text='Enter Mothers Name:',selectbackground="red").grid(row=1,column=4)

l3 = Label(text="Fathers Name:").grid(row=2,column=0)
e3 = Entry(text="Mother's Name:").grid(row=2,column=4)

b1 = Button(win,text="submit",bg="skyblue").grid(row=3,column=0)
# b1.pack()

win.mainloop()