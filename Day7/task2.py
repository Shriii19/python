a = int(input("entre a no:"))
org_no=a
rev = 0
while a > 0:
    dig = a % 10
    rev = rev * 10 + dig
    a=a//10
# print("rev is:" , rev)
if org_no == rev:
    print("palindrome")

else:
    print("not")


