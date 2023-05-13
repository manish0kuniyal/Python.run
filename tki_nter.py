#creates a body or a window

from tkinter import *
top=Tk()
top.mainloop()



#creating a button

from tkinter import *
top=Tk()
rbutton=Button(top,text='Rd',fg='red')
rbutton.pack(side=LEFT)
top.mainloop()



#creating a grid

from tkinter import*
parent=Tk()
rbtn=Button(parent,text="ppppp",fg='pink').grid(row=0,column=0)
name=Label(parent,text="yourname",bg='blue').grid(row=1,column=1)
e1=Entry(parent,bg='yellow').grid(row=2,column=0)
parent.mainloop()



#placing elements in the canvas or plane

from tkinter import*
build=Tk()
#size of canvas
build.geometry("400x400")
name=Label(build,text="name" ).place(x=100,y=0)
button=Button(build,text='click').place(x=300,y=100)
build.mainloop()


#display message

from tkinter import*
from tkinter import messagebox
build=Tk()
build .geometry("300x300")
def msg():
    messagebox.showinfo("henlo")

btn1=Button(build,text='red',bg='red',fg='white',command=msg())
btn2 = Button(build, text='re', bg='black', fg='white').place(x=200,y=100)

build.mainloop()
