#Ethan Eash
#9/20
#guess my number 1.0

import random

theNumber = random.randint(1,10)
#print(theNumber)#for testing remove when finished

win = False

print("\twelcome to 'guess my number'")
print("\nI'm thinking of a number between 1 and 10.")
print("try to guess it in 3 attempts.\n")

#guess 1
guess = int(input("pick a number between 1 and 10"))

if guess == theNumber:
    print("winner")
    win = True
elif guess > theNumber:
    print("guess lower")
else:
    print("guess higher")
#guess 2
if not win:
    guess = int(input("pick a number between 1 and 10"))

    if (guess == theNumber) and (not win):
        print("winner")
        win = True
    elif guess > theNumber:
        print("guess lower")
    else:
        print("guess higher")



#guess 3
if not win:
    guess = int(input("pick a number between 1 and 10"))

    if guess == theNumber:
        print("winner")
        win = True
    elif guess > theNumber:
        print("Loser")
        print("the number was",theNumber)
    else:
        print("loser")
        print("the number was",theNumber)










##print(guess)
##print(type(theNumber))
##print(type(guess))


