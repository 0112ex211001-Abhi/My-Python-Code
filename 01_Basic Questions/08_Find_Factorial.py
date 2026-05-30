""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

# way one to solve 
n = int (input ("Enter a number: "))
factorial = 1 

if n==0 or n==1 :
    factorial = 1
else:
    for i in range (1, n+1):
        factorial *= i

print (f"The factorial of {n} is {factorial}")

# way two to solve
n = int (input ("Enter a number: "))
factorial = 1

for i in range (1, n+1):
    if n==0 or n==1 :
        facrorial = 1 
    else:
        factorial *= i

print (f"The factorial of {n} is {factorial}")

# Modified by using Function
def factorial():

    if n == 0 or n == 1 :
            return f"The factorial of {n} is {1}"
    else:
        f = 1
        for i in range (1, n+1):
            f *= i
        return f"The factorial of {n} is {f}"

n = int(input("Enter a number to find the factorial value: "))
print(factorial())