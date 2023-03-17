from asyncio import sleep
import os
import time
import pickle
class rooms:
    def __init__(self,number,floor, area):
        self.number=number
        self.area=area
        self.floor=floor

room1=rooms(
    number=1,
    floor=1,
    area=85
)
room2=rooms(
    number=2,
    floor=2,
    area=120
)
room3=rooms(
    number=3,
    floor=2,
    area=85
)
room4=rooms(
    number=4,
    floor=3,
    area=120
)
room5=rooms(
    number=5,
    floor=2,
    area=85
)
room6=rooms(
    number=6,
    floor=3,
    area=120
)

empty_rooms=["room1","room3","room5","room6"]
full_rooms = ["room2","room4"]
while True:
    os.system("cls")
    print("------ m  e  n  u -----")
    print("1.Empty Rooms")
    print("2.Description Of Rooms")
    print("3.Get a Room")
    print("4.Tell Us Specifications in Question ")
    print("Some Facts About Our Hotel")
    print("5.Talk to Manager")
    print("6.Exit")
    number=int(input("Please select From 1-6:"))

    os.system("cls")
    if number == 1 :
        time.sleep(1.10)
        while True:
            print (empty_rooms)
            print("Exit == 0")
            select = int(input("Enter Number Of Room To See Specifications:"))
            
            if select == 1:
                print ("Number is:",room1.number)
                print ("Floor is:",room1.floor)
                print("area is:",room1.area)
                time.sleep(2)
            elif select == 2:
                print("Its Not Empty Room")
                print("Please Try Another")
                time.sleep(2)
            elif select == 3:
                print ("Number is:",room3.number)
                print ("Floor is:",room3.floor)
                print("area is:",room3.area)
                time.sleep(2)
            elif select == 4:
                print("Its Not  Empty Room")
                print("Please Try Another")
                time.sleep(2)
            elif select == 5:
                print ("Number is:",room5.number)
                print ("Floor is:",room5.floor)
                print("area is:",room5.area)
                time.sleep(2)
            elif select == 6:
                print ("Number is:",room6.number)
                print ("Floor is:",room6.floor)
                print("area is:",room6.area)
                time.sleep(2)
            elif select > 6:
                print("Sorry We Dont That Room")
                print("Please Select From The List")
                time.sleep(2)
            elif select ==0 :
                break
    elif number == 2:
        print("Room 1 : its clean Big With Wide Windows")
        print("Room 2 : its Not Well Made But it has Great Kitchen")
        print("Room 3 : Not a Great Windows But Trust Me its Bigger Than Other Rooms")
        print("Room 4 : Thats a Well-Made room With Garden And So Many Flowers")
        print("Room 5 : Walls With Nice Color Big Bathroom and a Well-made one ")
        print("Room 6 : full Option Room I can say its the Best Room we have and Actualy the Most Expensive")
        print("This Page will Disappear After 20 Seconds")
        time.sleep(20)

    elif number == 3 :
        print(empty_rooms)
        x = (input("Witch Room Do You Want?"))
        empty_rooms.remove(x)
        full_rooms.append(x)

        x=input("your name:")
        x2=input("last name:")
        x3=input("how many days:")
        x4=input("for how many people:")
        x5=input("Do you want special services:")
        x6=input("when do you want to come:")
        print("That Room Will Reserve For you Until You Pay For It")
        time.sleep(2)
        print("Thanks To Choose Our Hotel , Its An Honor")
        time.sleep(3)
    elif number == 4:
        print("Specifications and Questions")
        x = input ("Write Here:")
        time.sleep(1)
        print("Thanks For Sharing With US")
        time.sleep(3)
    elif number == 5:
        print("Hello Im Hashemi . the Hotels Manager , How Can I Do For You?:")
        answer=input("write everything You Want To Manager Read He Will Sends You Feed Back:")
        print("Thanks For Sharing Your Opinion With Us")
        time.sleep(3)
    elif number == 6:
        break
    else:
        print("Please Choose From The List")
        time.sleep(4)



        

