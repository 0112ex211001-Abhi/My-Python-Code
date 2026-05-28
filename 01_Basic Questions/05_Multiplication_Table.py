'''Multiplication Table by using for loop'''
n = int (input ("Enter a number: "))

for i in range (1, 11):
    product = n*i 
    print (f"{n} X {i} = {product}")

'''Multiplication Table by using while loop'''
a = int (input ("Enter a number: "))
i = 1
while i <= 10:
    product = a*i 
    print (f"{a} X {i} = {product}")
    i += 1
