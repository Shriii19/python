#Arithmetic Operators

a=10
b=20

print("Arithmetic Operators")

print( a+b ) 
print( a-b ) 
print( a*b ) 
print( a/b ) 

#***********************************************************************************************************

#Relational / Comparison Operators

print("Relational / Comparison Operators")

print(a==b)
print(a>b)
print(a<b)
print(a!=b)
print(a>=b)
print(a<=b)

#***********************************************************************************************************

#Assignment Operators

print("Assignment Operators")

c=15
c+=15 #just change the operates like -=,%=,&=,/=,**=

print(c)


#***********************************************************************************************************

#Logical Operators
 
# Not, And ,Or

#not will give opposite and like (true is there but finally output will false)

print("***Not operate")
print(not True) #ans will false
print(not False) #ans will true
print(not (a>b)) #ans will false


#this And operate will give ouput when both and satisfy 
print("***And operate")

val1=True
val2=True
val3=False

print(val1 and val2)
print(val2 and val3)

#this Or operate btn 2 value one is true it will give true only 
print("*** OR operate")
print(val2 or val3)