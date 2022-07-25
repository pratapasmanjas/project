# from operator import truediv
# from pickle import TRUE
import random
# import tkinter
from tkinter import FALSE, NONE ,TRUE
# from types import NONE
randNO = random.randint(1, 3)
print(randNO)
def gamewin (computer, you):
    if computer == you:
        return NONE
    elif computer == 'r':
        if you =='s':
            return FALSE
        elif you == 'p':
            return TRUE
    elif computer =='p':
        if you == 'r':
            return FALSE
        elif you == 's':
            return TRUE
    elif computer =='s':
        if you =='p':
            return FALSE
        elif you== 'r':
            return TRUE

print ("computer turn: Rock(r) paper(p) or scissor(s) ?")
randNO= random.randint(1, 3)
print(randNO)
if randNO == 1:
    computer = 'r'
elif randNO == 2:
    computer = 'p'
elif randNO == 3:
    computer = 's'
you = input("your turn: rock(r) paper(p) or scissor(s) ?")
a = gamewin(computer,you)
print(f" computer chose {computer}")
print(f" you chose {you}")
if a == NONE :
    print(" game is tai!")
elif a:
    print(" you are win")
else :
    print(" you loss !")
