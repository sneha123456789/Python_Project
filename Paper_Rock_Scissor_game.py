# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 00:18:57 2022

@author: Sneha Abraham
"""
#Paper Scissors Rock Game
import random

def gameWin(computer, you):
    #If two values are same declare a tie
    if computer == you:
        return None
    #Check for all possiblities when computer chooses s
    elif computer == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    #Check for all possibiliies when computer chooses w   
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'r': 
            return True
    #Check for all possibilities when computer chooses g     
    elif computer == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True
        
    
print("Computer Turn: Paper(p) Rock(r) or Scissorss(s)?")
randNo = random.randint(1, 3)
#print(randNo)
if randNo == 1:
    computer = 'p'
elif randNo == 2:
    computer = 'r'
elif randNo == 3:
    computer = 's'


you = input("Your Turn: Paper(p) Rock(r) or Scissors(s)?")

a = gameWin(computer, you)

print(f"Computer choose {computer}")
print(f"You choose {you}")

if a == None:
    print("Game is a tie")
elif a:
    print("You win")
else:
    print("You loose")
    
    
    