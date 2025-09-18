from tkinter import *
root = Tk()
# root.geometry("200x200")
root.title("Scrollbar")
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )

for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT)
scrollbar.config( command = mylist.yview )
root.mainloop()