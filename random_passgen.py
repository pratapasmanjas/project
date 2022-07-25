import string
import random

def password():
   s1 = string.ascii_lowercase
   s2 = string.ascii_uppercase
   s3 = string.punctuation
   s4 = string.digits
   s = []
   s.extend(list(s1))
   s.extend(list(s4))
   s.extend(list(s3))
   s.extend(list(s2))
   # print(s)
   random.shuffle(s)
   plen = int(input(" please enter your password length-\n"))
   print("".join(s[0:plen]))
if __name__ == "__main__":
   while True:
      password()
      choce = input(" do you want to roll the dice again (y/n) ")
      if choce.lower() == 'n':
         break