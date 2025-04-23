'''
    This is project to play rock-paper-scissors game with a computer.
    I hope you enjoy it.
'''

import random

def play():
    user = input("Enter your choice (r -> rock, p -> paper, s -> scissors): ")
    computer = random.choice(['r', 'p', 's'])
    
    if (computer == 's'):
        print("Computer chose -: scissors")
    elif (computer == 'r'):
        print("Computer chose -: rock")
    else:
        print("Computer chose -: paper")
    # print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!"
    
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        print("Sometime coputer also lost , next time")
        return "You won!"
    
    return "You lost!"

def is_win(player, computer):
    # return true if player wins
    
    # r > s, s > p, p > r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
        or (player == 'p' and computer == 'r'):
        return True
    
print(play())