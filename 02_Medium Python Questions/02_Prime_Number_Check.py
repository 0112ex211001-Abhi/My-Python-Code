""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""


n = int (input ("Enter a number: "))

if n > 1:
    for i in range (2,n):
        if n % i == 0:
            print (n, "is not a Prime Number.")
            break
    else:
        print (n, "is a Prime Number.")
else:
    print (n, "is not a Prime Number.")





if n > 1:
    for i in range (2, int (n ** 0.5)+1):
        if n % i == 0:
            print (n, "is not a Prime Number.")
            break
    else:
        print (n, "is a Prime Number.")
else:
    print (n, "is not a Prime Number.")




if n > 1 and n % 2 != 0:
    for i in range (3, int (n ** 0.5) + 1, 2):
        if n % i == 0:
            print (n, "is not a prime number.")
            break
    else:
        print (n, "is a prime number.")
else:
    print (n, "is not a prime number.")