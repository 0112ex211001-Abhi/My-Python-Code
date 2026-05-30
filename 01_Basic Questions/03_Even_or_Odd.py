""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

num = int (input ("Enter a number: "))

if num % 2 == 0:
    print (f"{num } is an even number.")
else:
    print (f"{num} is an odd number.")


# Modified by using Function
def EvenOrOdd(n):
    result = f"{n} is an {'even' if n % 2 == 0 else 'odd'} number."
    print(result)

n = int (input ("Enter Your Number: "))
EvenOrOdd(n)
