import random
options =["Rock","Paper","Scissors"]
userchoice =input("Rock,Paper,Scissors:")
computer_choice=random.choice(options)
print("Your choice",userchoice)
print("Computers choice",computer_choice)
if userchoice==computer_choice:
    print("It is tie")
elif userchoice=="Rock" and computer_choice=="Scissors":
    print("you win")
elif userchoice=="Paper" and computer_choice=="Rock":
    print("you win")
elif userchoice=="Scissors" and computer_choice=="Paper":
    print("you win")
else:
    print("You Lose")
    