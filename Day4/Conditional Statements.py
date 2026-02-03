name = str(input("enter your name"))
name = str(input("enter your college name"))

marks1 = int(input("enter your phy marks"))
marks2 = int(input("enter your chem marks"))
marks3 = int(input("enter your bio marks"))
Total=marks1+marks2+marks3


if marks1 >=90:
    print("grade is A")
    grade1="A"

elif marks1 >=80 and marks1 <=89:
    print("grade is B")
    grade1="B"

elif marks1 >=70 and marks1 <=79:
    print("grade is C")
    grade1="C"
else:
    print("grade is D need score more marks")




if marks2 >=90:
    print("grade is A")

elif marks2 >=80 and marks2<=89:
    print("grade is B")

elif marks2 >=70 and marks2 <=79:
    print("grade is C")

else:
    print("grade is D need score more marks")

if marks3 >=90:
    print("grade is A")

elif marks3 >=80 and marks3 <=89:
    print("grade is B")

elif marks3 >=70 and marks3 <=79:
    print("grade is C")

else:
    print("grade is D need score more marks")




print("welcome to result section see ur grade here")
print("Name:" , name)
print("college Name:" , name)
print(f"Your Marks for PHY is {marks1} and Grade is {grade1}")
print("your percentage:" , Total/4)



