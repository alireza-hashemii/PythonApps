# get input from user

year = int(input("Enter the year:-"))

# calculate if it's leap year or not

if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):

# return the answer

    print(f"{year} is a leap year.")
else:
    print(f"{year} it's not a leap year")