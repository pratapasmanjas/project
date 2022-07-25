import random

def rolldice(min, max):
    while True:
        print(" dice is rolling ........")
        number = random.randint(min, max)
        print(f" your no is {number}")
        choce = input(" do you want to roll the dice again (y/n) ")
        if choce.lower() == 'n':
            break

rolldice(1,6)