import datetime 
import smtplib
import time
import psycopg2
import random
from colorama import *

#? Connect to Database
connection = psycopg2.connect(database="hospital", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cursor = connection.cursor()


#TODO Base Class Of Program
class ReserveTime:
    def __init__(self,name,family,number,doctor,date,payed,registration,codingtrack):
        self.name = name
        self.family = family
        self.number = number
        self.doctor = doctor 
        self.date = date
        self.payed = payed
        self.registration = registration 
        self.codingtrack = codingtrack


doctors = ['david auth','nora kian','sam hana','lona siami','aria roohi','yai chi','rami moled','kia amiri','ana moali','kave kooshan']

while True:
    #! Program Starts 
    menu = int(input("""----- MENU -----\n
    1-LIST OF DOCTORS
    2-RESERVE A TIME
    3-CRITISM AND SUGGESTION
    4-SEE YOUR HISTORY
    6-WANNA SEE PEOPLES SUGGESTION ABOUT US?
    7-EXIT: """))

# todo Show list of doctors 
    if menu == 1:
        docnumber = -1
        for doctor in doctors:
            docnumber = docnumber + 1
            print(f"{docnumber}:",doctor, end="\n")

        next_move = int(input("Exit:0 Menu:1 >> "))
        if next_move == 1:
            print(Fore.CYAN,"redirecting...")
            time.sleep(3.5)
            pass
            
        elif next_move == 0:
            print(Fore.GREEN,"Thanks for choosing our app")
            break
        else:
            print(Fore.RED,"Choose from list please!")
            time.sleep(3)
            pass
    
    if menu == 2:
        sure_idea = int(input("are you sure? << y:1 OR n:0 >>: "))
        if sure_idea == 1 :
            
            sender_email = 'pyaireza7@gmail.com'
            receiver_email = input("Enter yor email: ")
            password = 'sdlrjodkrmawxgdc'
            password = str(password)
            message = str(random.randrange(11111111,99999999))
            int_email= int(message)
            # todo connect to smtp server and login to our email account
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login(sender_email,password)
            print(Fore.MAGENTA , "Loading...")
            server.sendmail(sender_email,receiver_email,message)
            print("Email has been sent to",receiver_email)
            time.sleep(5)
            email_code = int(input("Enter code that we sent for you: "))
            if email_code == int_email:
                print("please fill in the list with your specifications!")
                time.sleep(2)
                obj = ReserveTime(
                    input("Enter Your name: "),
                    input("Enter Your family: "),
                    int(input("Enter Your phone number: ")),
                    input("Enter Your doctors name: "),
                    datetime.datetime.now(),
                    30,
                    True,
                    email_code
                )
                print("Your reservation completed \n loading...")
                time.sleep(1.5)
                print(f"This is your tracking code:{obj.codingtrack}")
                time.sleep(3)
            else:
                print("sorry code was wrong! ")
                time.sleep(2)

        elif sure_idea == 0:
            print(Fore.GREEN,"Thanks!")
            time.sleep(3)
            break

        else:
            print("please choose from the list")
            time.sleep(3)
    
    if menu == 3:
        print("loading the box...")
        time.sleep(2)
        critism_box = input("Enter your suggestion and critistm: ")
        your_name = input("Enter your name: ")
        try:
            cursor.execute(f"INSERT INTO critism(name,content) \
                VALUES ('{your_name}','{critism_box}')");
            connection.commit()
            sender_email = 'pyaireza7@gmail.com'
            receiver_email = input("Enter yor email: ")
            password = 'sdlrjodkrmawxgdc'
            password = str(password)
            message = "Thanks for sharing your opinion we will fix the problem"
            # todo connect to smtp server and login to our email account
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login(sender_email,password)
            print(Fore.MAGENTA , "Loading...")
            server.sendmail(sender_email,receiver_email,message)
            print(Fore.GREEN,"your opinion saved we will answer you in couple of days!")
        except BaseException:
            raise(TypeError)
    
    if menu == 4:
        account = int(input("you have account? yes:1 no:0 "))
        if account == 1:
            name = input("Enter your name: ")
            cursor.execute(f"SELECT *  from onlinetimetable WHERE name='{name}'")
            rows = cursor.fetchall()
            for row in rows:
                print ("name = ", row[0])
                print( "family = ", row[1])
                print ("number = ", row[2])
                print ("doctor = ", row[3])
                print ("payed = ", row[4])
                print ("registration = Done")
                print ("coding track = ", row[6], "\n")
               
            print(Fore.GREEN,"Operation done successfully")
            time.sleep(5)
    if menu == 5:
        cursor.execute("SELECT *  from critism")
        rows = cursor.fetchall()
        for row in rows:
            print ("name = ", row[0])
            print ("suggestion = ", row[1], "\n")
            time.sleep(5)
    
    if menu == 6:
        print("Thank's for using our app Good luck! ")
        time.sleep(2)  
        break
    
cursor.close()



   
        


