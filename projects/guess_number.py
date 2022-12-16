import random

laps = 10
number_of_guesses = 1

for i in range(laps):
    random_number = random.randint(0,5)
    user_number = int(input("Enter a number in range 0-10: "))
    if random_number == user_number:
        print(f"Congrats you have guessed right with {number_of_guesses} guesses.")
        break
    else:  
        number_of_guesses += 1
        continue
