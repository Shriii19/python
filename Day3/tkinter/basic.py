import tkinter
from tkinter import messagebox
from tkinter import *

top=Tk()
top.geometry("325x200")
top.title("My first GUI")
top['bg'] = 'light blue'
uname=Label(top,text="Name",).place(x=30,y=50)
uage=Label(top,text="Age").place(x=30,y=80)
umno=Label(top,text="Mno:").place(x=30,y=110)
uname=Entry(top).place(x=100,y=50)
uage=Entry(top).place(x=100,y=80)
umno=Entry(top).place(x=100,y=110)

def myfunc():
    messagebox.showinfo("thank you","Your form has been submitted")
btn=Button(top,text="Submit",command=myfunc).place(x=120,y=150)
top.mainloop()