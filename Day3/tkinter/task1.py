import tkinter
from tkinter import messagebox
from tkinter import *

top=Tk()
top.geometry("500x500")
top['bg']="#51E1DC"

Label( top,text="first no" , width="13").place(x=50,y=50)
ent1=Entry(top)
ent1.place(x=150,y=50)

Label( top,text="second no" , width="13").place(x=50,y=80)
ent2=Entry(top)
ent2.place(x=150,y=80)




# logical
def myfun():
        num1 = int(ent1.get())
        num2 = int(ent2.get())
        messagebox.showinfo("sum:", (num1 + num2))

btn=Button(top,text="Add",width="13", command=myfun).place(x=100,y=120)    

top.mainloop()
