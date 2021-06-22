import random

question = input("What is your question that requires answering: ")
start = input("Shake the eight to see your destiny that awaits: ").lower()
    
if start == "shake":
    dice = random.randint(1, 8)
    if dice == 1:
        print("It is certain.")
    if dice == 2:
        print("It is decidely so.")
    if dice == 3:
        print("Without a doubt.")
    if dice == 4:
        print("Yes, definately")
    if dice == 5:
        print("You may rely on it.")
    if dice == 6:
        print("As I see it, yes.")
    if dice == 7:
        print("Most likely.")
    if dice == 8:
        print("Outlook good.")
else:
    print("Please shake the ball.")