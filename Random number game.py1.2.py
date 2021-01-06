#Ethan Eash
#9/20
#guess my number 1.0

import random

##theNumber = random.randint(1,maxNumber)
#print(theNumber)#for testing remove when finished

#setting variables
maxNumber = 10
numTrys = 3
diff = 1



win = False

print("\twelcome to 'guess my number'")


#difficulty settings
question = input("what difficulty owuld you like Easy, Medium, Hard ")

if question.startswith("E") or question.startswith("e"):
    maxNumber = 10
    numTrys = 3
    diff = 1
elif question.startswith("M") or question.startswith("m"):
    maxNumber = 50
    numTrys = 5
    diff = 2
else:
    maxNumber = 100
    numTrys = 10
    diff = 3

theNumber = random.randint(1,maxNumber)




print(str.format("\nI'm thinking of a number between 1 and {}.",maxNumber))
print(str.format("try to guess it in {} attempts.\n",numTrys))
#guess 1
guess = int(input("pick a number between 1 and " + str(maxNumber)))

if guess == theNumber:
    print("winner")
    win = True
elif guess > theNumber:
    print("guess lower")
else:
    print("guess higher")
#guess 2
if not win:
    guess = int(input("pick a number between 1 and " + str(maxNumber)))

    if (guess == theNumber) and (not win):
        print("winner")
        win = True
    elif guess > theNumber:
        print("guess lower")
    else:
        print("guess higher")
#guess 3
if not win:
    if diff == 2:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 4
if not win:
    if diff == 2:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 5
if not win:
    if diff == 2:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 6
if not win:
    if diff == 3:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 7
if not win:
    if diff == 3:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 8
if not win:
    if diff == 3:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")
#guess 9
if not win:
    if diff == 3:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

        if (guess == theNumber) and (not win):
            print("winner")
            win = True
        elif guess > theNumber:
            print("guess lower")
        else:
            print("guess higher")

#Last guess
if not win:
    if diff == 3:
        guess = int(input("pick a number between 1 and " + str(maxNumber)))

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


