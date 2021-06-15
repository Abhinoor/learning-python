import random 

#Wlecoming User to the game
print("Welcome to RNG Guessing Championship")

#Creating a loop that starts by the computer generating a random number between 1 and 50 and the user typing in their number between 1 and 50.
while True:
    computer = random.randint(1, 50) 
    userChoice = int(input("Guess a number between 1 and 50: "))
    #If the user gets the number the computer generated then they are congradulated and the loop breaks/stops.
    if userChoice == computer: #user guesses correctly
        print("Congrats you are now an RNG Champion.")
        break
    else: #user guesses incorrectly
        #If the user guesses incorrectly within the range they will be asked if they would like to continue or quit.
        if userChoice >= 1 and userChoice <= 50:
            rage = input("Sorry that is inccorect. Would you like to continue playing? ").lower()
            if rage == "yes":
                continue
            if rage == "no":
                break
        #If the user guesses outside of the range they will be encouraged to guess within the range and the loop will retart.
        else:
            print("Please choose a number within the range.")
    


# user gusses corectly
# user guesses incorrectly
    # they guess incorectly but within the range
    # they guess outside of the range