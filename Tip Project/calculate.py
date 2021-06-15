#Here we begin by asking the user for the total bill
total = float(input("What's the total bill for today: $"))

#The cost variables are set equal to the total cost plus the different percent tips. The tip varaibles are set equal to the total tip.
cost1 = round(total * 1.18, 2)
tip1 = round(total * .18, 2)

cost2 = round(total * 1.20, 2)
tip2 = round(total * .20, 2)

cost3 = round(total * 1.25, 2)
tip3 = round(total * .25, 2)

#Here we print out the prices at different percentages for both the total of the bill and tips.
print(f"A 18% tip will be ${tip1}, brining the total cost to ${cost1}")
print(f"A 18% tip will be ${tip2}, brining the total cost to ${cost2}")
print(f"A 18% tip will be ${tip3}, brining the total cost to ${cost3}")