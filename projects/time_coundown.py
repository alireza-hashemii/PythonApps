import time 
# core of program find (min) and (sec) with divmod func.

def countdown(t):
    while t:
        minutes , seconds = divmod(t,60)
        timer = f'{minutes}:{seconds}'
        print(timer,end="\r")
        time.sleep(1)
        t -= 1

    print("Time Completed!")

# input seconds from the user

t = input("Enter time in seconds: ")
countdown(int(t))