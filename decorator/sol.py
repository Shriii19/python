def decorator(funs):
    def wapper():
        print("hellooo")
        funs()
        print("payment done")
    return wapper

@decorator
def hey():
    print("hello how are you")
    print("payment is going on")
hey()

# A decorator in Python is a special type of function that can modify or enhance the behavior of another function. 
# It allows you to "wrap" a function with additional functionality without changing the original function's code. 