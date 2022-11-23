from tkinter import *
def fun():
    print("This is my fuction")
win = Tk()

win.geometry('500x500')
# bd&bg
# c1 = Canvas(bd=200,bg="red").grid(row=0,column=0)
# confine->getting error
# c2=Canvas(bd=500,bg="blue",confine=SCROLL).grid(row=1,column=0)
# cursor-arrow,circle,dot
# c3= Canvas(bg="red",bd=200,cursor="circle").grid(row=2,column=0)
# height
# c4 = Canvas(bg="blue",height=200,cursor="dot").grid(row=3,column=0)
# highlightcolor
# c5= Canvas(highlightcolor="blue",bg="gray",height=200).grid(row=4,column=0)
# refief- SUNKEN, RAISED, GROOVE, and RIDGE.
# c6= Canvas(bg="gold",bd=200,relief=RIDGE).grid(row=5,column=0)
# scrollregion-Getting errror
# c7= Canvas(bg="blue",scrollregion=(1,5,80)).grid(row=6,column=0)
# width
# c8= Canvas(bg="red",width=150,cursor="arrow").grid(row=7,column=0)
# xscrollincrement-> not understand
# c9= Canvas(bg="blue",width=200,xscrollincrement=set())
# yscrollincrement
# c10= Canvas(bg="red",).grid(row=9,column=0)
# xscrollcommand
# c11= Canvas(bg="blue",xscrollcommand=fun()).grid(row=10,column=0)
# yscrollcommand
# c12= Canvas(bg="red",yscrollcommand=fun()).grid(row=11,colume=0)


c13 = Canvas(win,bg="blue",height=500,width=500)
arc= c13.create_arc((5,10,200,300),start=0,extent=200,fill="red")
c13.pack()

# c = Canvas(win,bg = "pink",height = "200",width = 200)  
  
# arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
  
# c.pack()  

win.mainloop()