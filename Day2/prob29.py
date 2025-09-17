#WAP remove item into tuple 
a=("apple", "banana", "cherry")
b=list(a)
b.remove("banana")
a=tuple(b)
print(a)