n = int (input ("Enter a number: "))

factorial = 1 
if n==0 or n==1 :
    factorial = 1
else:
    for i in range (1, n+1):
        factorial *= i

print (f"The factorial of {n} is {factorial}")


# factorial = 1

# for i in range (1, n+1):
#     if n==0 or n==1 :
#         facrorial = 1 
#     else:
#         factorial *= i

# print (f"The factorial of {n} is {factorial}")