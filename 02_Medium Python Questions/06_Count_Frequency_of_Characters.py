# Count the frequency of each character in a string
def count_frequency(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result = count_frequency(input_string)
    for char, freq in result.items():
        print(f"'{char}': {freq}")

