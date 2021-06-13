#Here we import the random module so we can get the computer to randomly choose between rock, paper, and scissors.
import random

#Here we set the choices variable equal to a list comprised of rock, paper, and scissors.
choices = ["rock", "paper", "scissors"]
#Here a computer varaible is set equal to random.choice which randomly selects one of the three options from the list.
computer = (random.choice(choices))

#A simple print statement to welcome the user into the game.
print("Welcome to the Rock, Paper, Scissors Game")

'''
We then define a new userChoice varaible that is equal to the input that a user puts 
in and we make it run through the code as lower case using the .lower() method.
'''
userChoice = input("Your Choice: ").lower()
#Here we tell the user the random choice the computer made using a print statement.
print("Computers choice:", computer)

#Lastly we define the series of possible outcomes and set the winning and losing configurations.
if userChoice == "rock":
    if computer == "rock":
        print("Draw. Rock can't beat rock.")
    if computer == "scissors":
        print("Rock beats scissors. You win!")
    if computer == "paper":
        print("Rock can't beat paper. You lose :(")
elif userChoice == "scissors":
    if computer == "rock":
        print("Scissors can't beat rock. You lose :(")
    if computer == "scissors":
        print("Draw. Scissors can't beat scissors.")
    if computer == "paper":
        print("Scissors beats paper. You win!")
elif userChoice == "paper":
    if computer == "rock":
        print("Paper beats rock. You win!")
    if computer == "scissors":
        print("Paper can't beat scissors. You lose :(")
    if computer == "paper":
        print("Draw. Paper can't beat paper.")