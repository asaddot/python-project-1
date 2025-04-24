# this is project - guessing the number game
# user choose two numbers which will be range 
# computer will choose the number in that range
# user will guess the number it have total 3 guesses

import random

def guess_number():
    
    print("Welcome to the Guess the Number Game!")
    print("Select a range from 1 to 100")
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    computer_guess = random.randint(a,b)
    print(f"Computer has selected a number between {a} and {b}.")
    
    print("You have 3 chances to guess the number.")
    
    print("Life : 3")
    l = 3
    
    for i in range(3):
        
        
        user_guess = int(input("Enter your guess: "))
        if user_guess == computer_guess:
            print("Congratulations! You guessed the number correctly.")
            break
        elif user_guess < computer_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        # print("Life : ", l-1)
    
        l -= 1
        if l == 0:
            print("Game Over! The correct number was:", computer_guess)
            break
        else:
            print("You have", l, "lives left.")
            
            
if __name__ == "__main__":
    guess_number()