from tkinter import *
root =Tk()
root.geometry("200x150")
root.title("Radio Button")
v=IntVar()
Radiobutton(root,text='Google',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='Yahoo',variable=v,value=2).pack(anchor=W)

mainloop()  

