""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""


# Remove duplicates from list

# Method 1: Using set()
def remove_duplicates_set(lst):
    return list(set(lst))


# Method 2: Using dict.fromkeys() - preserves order
'''Best method or code for solving this question bcz it fast , easy and preserves the order'''
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))


# Method 3: Using loop with membership test
def remove_duplicates_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# Method 4: Using list comprehension with index
def remove_duplicates_index(lst):
    return [item for index, item in enumerate(lst) if item not in lst[:index]]


# Test cases
if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]
    
    print("Original list:", test_list)
    print("Method 1 (set):", remove_duplicates_set(test_list))
    print("Method 2 (dict.fromkeys):", remove_duplicates_dict(test_list))
    print("Method 3 (loop):", remove_duplicates_loop(test_list))
    print("Method 4 (index):", remove_duplicates_index(test_list))


