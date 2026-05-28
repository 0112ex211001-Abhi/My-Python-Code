# Sort a list without using sort() - Bubble Sort Algorithm

# Step 1: Original unsorted list
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

# Step 2: Get the length of the list
n = len(numbers)

# Step 3: Outer loop - repeats for each element in the list
for i in range(n):
    # Step 4: Inner loop - compares adjacent elements
    # range(n - i - 1) ensures we don't compare already sorted elements
    for j in range(0, n - 1):
        # Step 5: Compare adjacent elements
        # If left element is greater than right element, swap them
        if numbers[j] < numbers[j + 1]:
            # Step 6: Swap the elements using temporary variable

            # temp = numbers[j]
            # numbers[j] = numbers[j + 1]
            # numbers[j + 1] = temp

            numbers[j], numbers[j+1] = numbers[j + 1], numbers[j]

# Step 7: Print the sorted list
print("Sorted list:", numbers)

# print("\n--- EXPLANATION LINE BY LINE ---")
# print("1. numbers = [64, 34, 25, 12, 22, 11, 90]  → Original list")
# print("2. n = len(numbers)  → n = 7 (list length)")
# print("3. for i in range(n)  → Loop 7 times")
# print("4. for j in range(0, n - i - 1)  → Compare adjacent pairs")
# print("5. if numbers[j] > numbers[j + 1]  → Check if left > right")
# print("6. swap elements using temp variable  → Exchange their positions")
# print("7. After all iterations, list becomes sorted in ascending order")
# print("\nThis is called BUBBLE SORT - larger elements 'bubble' to the end")





# n = [5, 2, 8, 1, 9]

# for i in range(len(n)):
#     for j in range(len(n) - 1):

#         if n[j] > n[j + 1]:

#             n[j], n[j + 1] = n[j + 1], n[j]

# print(n)





# numbers = [5, 2, 8, 1, 9]

# n = len(numbers)

# for i in range(n):

#     swapped = False

#     for j in range(0, n-i-1):

#         if numbers[j] > numbers[j+1]:

#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#             swapped = True

#     if not swapped:
#         break

# print(numbers)
