"""this code

     will ask for the typed numbers and check the following conditions:
         whether the entered string is a valid number,
         whether the user has not entered this number previously,
         whether the number is in the range 1-49,
     after entering 6 numbers, it will sort them in ascending order and display on the screen,
     will draw 6 numbers from the range and display them on the screen,
     will tell the player how many numbers he hit."
"""

import random

selected_numbers = []
i = 0

while i < 6:
    try:
        number = int(input("Put the number: "))
    except ValueError:
        print("It's not a number")
        continue
    if number > 49:
        print("Put the correct number")
        continue
    elif number in selected_numbers:
        print("Number already selected")
        continue
    else:
        selected_numbers.append(number)
    i += 1

print("Your selected numbers: ", sorted(selected_numbers))

randomly_selected_numbers = []
x = 0
z = random.randrange(1, 49)

while x < 6:
    z = random.randrange(1, 49)
    if z not in randomly_selected_numbers:
        randomly_selected_numbers.append(z)
    else:
        continue
    x += 1

print("Randomly selected numbers: ", sorted(randomly_selected_numbers))

winning_numbers = []

for number in randomly_selected_numbers:
    if number in selected_numbers:
        if number not in winning_numbers:
            winning_numbers.append(number)

print("Winning numbers: ", winning_numbers)

if len(winning_numbers) == 3:
    print("Congratulations! You have 3 winning numbers !")
elif len(winning_numbers) == 4:
    print("Congratulations! You have 4 winning numbers !")
elif len(winning_numbers) == 5:
    print("Congratulations! You have 5 winning numbers !")
elif len(winning_numbers) == 6:
    print("Congratulations! You have 6 winning numbers !")
else:
    print("You won nothing.")
