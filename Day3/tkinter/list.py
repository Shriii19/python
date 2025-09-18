from tkinter import *
Top = Tk()
Top.geometry("500x250")
Top.title("List Box")
lab = Listbox(Top)
lab.insert(1, 'Python')
lab.insert(2, "Java")
lab.insert(3, "C++")    
lab.insert(4, "C#")
lab.insert(5, "JavaScript")
lab.pack()

Top.mainloop()

