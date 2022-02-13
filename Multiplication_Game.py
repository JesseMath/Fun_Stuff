#Starts with 2 digit multiplication, after _ done correctly, you get 3 digits (or 2 and 3), after _ of these, move up, etc...

#Needs: timer

import random
import time

def two():
    n = random.randrange(1,100)
    m = random.randrange(1,100)

    print (str(n) + " times " + str(m))
    start = time.time()
    answer = input()
    end = time.time()
    elapsed = end - start
    if answer == n*m:
        print("Correct! In " + str(elapsed))
    else:
        print("Incorrect. The answer was " + str(n*m) + ". (you answered in " + str(elapsed) + ")")

    return

print("Welcome to the multiplication game! Please select your game.")

choice = input()

if choice == "two":
    print(two())

if choice == "three":
    print("I am sorry, that game is not ready yet.")