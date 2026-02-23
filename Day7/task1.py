class clgdb:
    new_clgname = "abc clg"
    def __init__(self, name , last_name, mobile_no, clg_name):
        self.name = name
        self.last_name = last_name
        self.mobile_no = mobile_no 
        self.clg_name = clg_name

s1=clgdb ("shree" , "patil", 1236547890, "xuzclg")
print(s1.name, s1.last_name, s1.mobile_no, s1.clg_name)
print(s1.new_clgname)