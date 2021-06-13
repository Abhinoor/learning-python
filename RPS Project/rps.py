import random

choice = ("rock", "paper", "scissors")
computer = (random.choice(choice))

print("Welcome to the Rock, Paper, Scissors Game")

user = input("Your Choice: ").lower()
print("Computers choice:", computer)

if choice == "rock" and computer == "scissors":
    print("Rock beats scissors. You win!")
elif choice == "scissors" and computer == "rock":
    print("Scissors can't beat rock. You lose!")
elif choice == "paper" and computer == "rock":
    print("Paper beats rock. You Win!")
elif choice == "rock" and computer == "paper":
    print("Rock can't beat paper. You lose!")
elif choice == "scissors" and computer == "paper":
    print("Scissors beats paper. You Win!")

if choice == "rock":
    #rock
    #scissors
    #paper
    print("Rock beats scissors. You win!")
elif choice == "scissors":
    print("Scissors can't beat rock. You lose!")
elif choice == "paper":
    print("Paper beats rock. You Win!")