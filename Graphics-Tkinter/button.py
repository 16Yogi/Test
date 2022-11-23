from tkinter import *


def fun():
    print("Hello this is my test function")

win = Tk()

win.geometry('1500x1500')
# active button
b1= Button(win,activebackground="blue",text="submit").grid(row=0,column=0)
# .place(height=30,width=70)
# b1.grid(row=0,colume=0)

# activeforground
b2= Button(win,activeforeground="red",text="activeforground").grid(row=1,column=0)
# .place(height=30,width=120)
# b2.grid(row=1,colume=0)

# bd-borderwidth
b3= Button(win,bd=10,text="Borderwidth").grid(row=2,column=0)

# bg- backgoundcolor
# b4= Button(win,bg="gold",bd=20,activeforeground="red",text="backgoundColor").grid(row=3,column=0)

# command
# b5= Button(win,bg="red",bd=20,activebackground="pink",activeforeground="blue",text="Command",command=fun()).grid(row=4,column=0)

# fg
b6= Button(win,fg="red",text="fg").grid(row=5,column=0)

# Font
b7= Button(win,font=50,fg="white",bg="black",text="Font").grid(row=6,column=0)

# height
# b8= Button(win,font=20,height=10,bg="skyblue",text="Height").grid(row=7,column=0)

# highlightcolor
# b9= Button(win,highlightcolor="red",text="highlightcolor",activeforeground="blue").grid(row=8,column=0)
# imge
# b10=Button(win,image="a.jpg",text="img").grid(row=9,column=0)
# (Image.open('images/sasuke.png')

# justify center,left,right
# b11= Button(win,justify=LEFT,text="justify",bg="blue").grid(row=10,column=0)

#padx-padding
b12= Button(win,padx=20,text="padding",bd=50).grid(row=11,column=0) 

# pady-padding
b13= Button(win,pady=10,bd=20,text="padding").grid(row=12,column=0)

# relief-SUNKEN, RAISED, GROOVE, and RIDGE.
b14= Button(win,relief=SUNKEN,text="relief").grid(row=13,column=0)

# state active&disable
b15= Button(win,state=DISABLED,text="state").grid(row=14,column=0)

# UNDERLINE->getting error
# b16= Button(win,underline=UNDERLINE,text="underline").grid(row=15,column=0)

b17= Button(win,width=100,text="width",bg="blue",activebackground="red",bd=20).grid(row=16,column=0)

# wraplenght
b18= Button(win,width=100,wraplength=20,bg="blue",text="wraplenght").grid(row=17,column=0)
win.mainloop()


