# Python Program to generate random number between 1 to 6 (simulating a dice)

import random
while True:
    ch = input("Want to generate number (y or n) : ")
    if ch.lower() == "y":
        print(f"Number is : {random.randint(1, 6)}")
    else:
        break