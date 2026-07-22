a =  input("Enter the No:")

try:
    for i in range (1, 11):
        print(f" {int(a)} X {i} = {int(a)*i}")
except ValueError:
    print("Please enter a valid integer.")



# Exception handling in Python is a mechanism that allows developers to manage and respond to runtime errors in a controlled manner. It helps prevent the program from crashing and provides a way to gracefully handle unexpected situations. The primary components of exception handling in Python are:
# 1. **try block**: This is where you write the code that might raise an exception. If an error occurs within this block, the control is transferred to the corresponding except block.
# 2. **except block**: This block contains the code that executes if an exception occurs in   the try block. You can specify the type of exception you want to catch, or use a general except block to catch all exceptions.
# 3. **else block**: This optional block runs if no exceptions were raised in the try block. It is useful for code that should only execute when the try block succeeds.
# 4. **finally block**: This optional block runs regardless of whether an exception occurred or not. It is typically used for cleanup actions, such as closing files or releasing resources.  