import random

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess=input("Guess a Number ")
    if int(guess) == number:
        isGuessRight = True
        print("Correct! The number was {}".format(number))
    else:
        print("Sorry, you guessed {}. This isn't right".format(guess))
        
        
