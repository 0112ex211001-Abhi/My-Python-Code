# a = int (input ("Enter number a: "))
# b = int (input ("Enter number b: "))

# sum = a + b 

# print (f"The sum of {a} and {b} is {sum}")

def add(a, b):
    sum = a + b
    return sum

a = int (input ("Enter number a: "))
b = int (input ("Enter number b: "))
result = add(a, b)
print (f"The sum of {a} and {b} is {result}")