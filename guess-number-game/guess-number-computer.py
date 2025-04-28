#  Guess the number game by computer
# here computer will choose the range
# user will guess the number 
# computer have 3 chances to guess the number

import random

def guess_number():
    a  = random.randint(1, 100)
    b  = random.randint(1, 100)
    if a > b:
        a, b = b, a
    print("Welcome to the Guess the Number Game!")

    print("Choose the number between", a, "and", b)
    num = int(input("Enter the number: "))

    lives = 3
    while lives > 0:
        computer_guess = random.randint(a, b)
        if computer_guess == num:
            print("Computer guessed the number correctly!")
            break
        elif computer_guess < num:
            print("Computer's guess is too low.")
        else:
            print("Computer's guess is too high.")

        lives -= 1
        if lives == 0:
            print("Game Over! The correct number was:", num)
            break
        else:
            print("Computer has", lives, "lives left.")
if __name__ == "__main__":
    guess_number()