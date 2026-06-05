""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

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


# Modified by using Function
def Table(n):
    return [f"{n} X {i} = {n * i}" for i in range(1, 11)]
# n= 5 , to return function return karega list ke form me :
# [5 X 1 = 5, 5 X 2 = 10, 5 X 3 = 15,...]
n = int(input("Enter a number: "))

for line in Table(n):
    print(line)
# jo return huaa hai use for loop line by line print kar dega
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15,...

print(*Table(n), sep="\n")
# '*' ye star phle list ko 5 X 1 = 55 X 2 = 105 X 3 = 15... kuch is tarike se todega 
# aur fir 'sep="\n"' use seprate karke line by line store karega
# aur print function print kardega 
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15,...