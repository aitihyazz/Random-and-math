import random
playing =True
number = str(random.randint(10,20))
print("I will genetarte a number from 10 to 20.You have to guess it")
print("The game is going to end When you guess it")
while playing:
    guess =input("GIve me your guess:)\n")
    if number==guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Try again:)")