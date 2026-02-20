def fact(n):
    if(n==1 or n==0):
        return 1
    return fact (n-1)*n

print(fact(5))

# what is Recursion? in simple terms, recursion is a programming technique where a function calls itself in order to solve a problem. 
# It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
#  This allows for elegant and efficient solutions to problems that can be defined in terms of smaller instances of the same problem.