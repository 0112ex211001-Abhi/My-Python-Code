'''Computer randomly chooses a number and user guesses it.

Use:
import random'''

import random
def guess_the_number(n):
    computer = random.randint(1,10)

    if computer == n:
        print("You win!")
    elif computer != n:
        print("You lose!")
    else:
        print("Invalid input! Please enter a number between 1 and 10.")    

    print(f"Computer's number is {computer}")

n= int (input("Enter your number btw 1 to 10 : "))
guess_the_number(n)