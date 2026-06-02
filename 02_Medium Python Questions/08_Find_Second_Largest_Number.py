""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""


def find_second_largest(numbers):
    if len(numbers) < 2:
        return "Error: At least two numbers are required."

    first_largest = second_largest = float('-inf')

    for num in numbers:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "Error: All numbers are the same."
    
    return f"Second largest number is: {second_largest}"
numbers = []
nlimit = int(input("Enter how many number you have: "))
while len(numbers) < nlimit:
    n = int(input("Enter your number one-by-one: "))
    numbers.append(n)
    # numbers.sort()

print(len(numbers))
print(find_second_largest(numbers))
           