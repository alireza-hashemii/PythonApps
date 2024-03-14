from math import ceil
number = int(input("Enter a number: "))

if number in range(1,187):
    day = number % 31 if number % 31 != 0 else 31
    month = number / 31
    print(f"Day is {day}")
    print(f"Month is {ceil(month)}")

elif number in range(187, 367):
    n_new = number - 186
    day = n_new % 30 if n_new % 30 != 0 else 30
    month = n_new / 30
    print(f"Day is {day}")
    print(f"Month is {ceil(month) + 6}")