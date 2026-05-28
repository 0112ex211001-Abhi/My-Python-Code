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
    
    return second_largest