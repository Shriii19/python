# & operator meaning bitwise AND
a = 10        # 1010 in binary  
b = 4         # 0100 in binary
c = a & b
print("a & b = ", c)

# | operator meaning bitwise OR
a = 10        # 1010 in binary  
b = 4         # 0100 in binary
c = a | b
print("a | b = ", c)

# ^ operator meaning bitwise XOR
a = 10        # 1010 in binary  
b = 4         # 0100 in binary
c = a ^ b
print("a ^ b = ", c)
# ~ operator meaning bitwise NOT
a = 10        # 1010 in binary
c = ~a
print("~a = ", c)   

# << operator meaning left shift
a = 10        # 1010 in binary
c = a << 2    # Shift left by 2 bits 
print("a << 2 = ", c) 

# >> operator meaning right shift
a = 10        # 1010 in binary
c = a >> 2    # Shift right by 2 bits
print("a >> 2 = ", c)