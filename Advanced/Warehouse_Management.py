# import needed libraries
import time
from colorama import Fore
import psycopg2
import datetime

# connect to Database with psycopg2
connection = psycopg2.connect(database="chart", user="postgres", password="1234", host="127.0.0.1", port="5432")
# Making Cursor To Work With Database
cursor = connection.cursor()

class Product:
    def __init__(self , name , id , price , date_joined):
        self.name = name
        self.id = id 
        self.price = price 
        self.date_joined = date_joined        

while True:
    User_selection = int(input(""" ---- MENU STOREROOM ----
            1- Add a product 
            2- List of products
            3- delete a product 
            4- Show product description 
            5- Update specific Product 
            6- Exit \n
            Enter a number from the list: """))
# add a product to db.

    if User_selection == 1:
        user_product = Product(
            input("Enter name of product: "),
            int(input("Enter Id of product: ")),
            int(input("Price of Product: ")),
            datetime.datetime.now()
        )
        date = user_product.date_joined.strftime("%x")
        name , id , price , date_joined = str(user_product.name) , int(user_product.id) , int(user_product.price) , date

        cursor.execute(f"INSERT INTO Product (name,id,price,datejoined) \
            VALUES ('{name}',{id},{price},'{date_joined}')");
        connection.commit()
        print (Fore.GREEN + "Operation Done successfully")
        time.sleep(1)
        cursor.close()

# show list of products

    if User_selection == 2:
            cursor.execute("SELECT * from Product")
            rows = cursor.fetchall()
            rows = list(rows)
            if len(rows) >= 1:
                for row in rows:
                    print ("Name = ", row[0])
                    print ("Id = ", row[1])
                    print ("Price = ", row[2])
                    print ("Date Joined = ", row[3])
                    print("--------------------------------")
            else:
                print(Fore.RED + "Sorry List has no Products !")
            time.sleep(3.5)  
            cursor.close()  

# delete product
    if User_selection == 3:
        result = input(Fore.YELLOW + "Show The Results After Proccess? yes/no: ")
        if result == "yes":

                User_deleted_record = (input("Which Product You want To Delete Enter It's Id: "))
                id = int(User_deleted_record)             
                cursor.execute("DELETE from Product where id=id;")
                print (f"Total number of rows deleted :{cursor.rowcount}")
                connection.commit()
                print(Fore.RED + "Product Deleted sucusfully and it's the result!","\n")
                cursor.execute("SELECT name,id,price, datejoined  from Product")                    
                rows = cursor.fetchall()
                for row in rows:
                    print ("Name = ", row[0])
                    print ("Id = ", row[1])
                    print ("Price = ", row[2])
                    print ("Date Joined = ", row[3])
                    print("--------------------------------")
                time.sleep(4)
                cursor.close()        
        elif result != 'yes' and 'no':
            print(Fore.RED , "please Choose from legal options!")
        else:
            User_deleted_record = (input("Which Product You want To Delete Enter It's Id: "))              
            cursor.execute("DELETE from Product where id=id;")
            connection.commit()
            print(Fore.RED + "Product Deleted succusfully! ")
        time.sleep(1)
        cursor.close()

# see on product details

    if User_selection == 4:
        which_product = int(input("Which Product Description you Want to see Specificly: it's id: "))
        id = int(which_product)
        try:
            product_detail = cursor.execute("SELECT * FROM Product  WHERE id=id")
            product_detail = str(product_detail)
            rows = cursor.fetchone()
            print(f"name: {rows[0]}")
            print(f"id: {rows[1]}")
            print(f"Price: {rows[2]}")
            print(f"date Joined: {rows[3]}")
        except(Exception):
            print(Fore.RED + "Sorry - no Product !")
        time.sleep(4)
        cursor.close()

# change detail of product

    if User_selection == 5:
        which_product = (input("Which Product you Want to make change Specificly: it's id: "))
        id = int(which_product)
        change_part = int(input("Enter 1 for name - 2 for id - 3 for price: "))
        if change_part == 1:
            new_name = input("Enter new name: ")
            cursor.execute(f"UPDATE Product set name = '{new_name}' WHERE   id = {id}")
            print ("Total number of rows updated :", cursor.rowcount)
            connection.commit()
            print(Fore.GREEN, "It changed successfully")
            time.sleep(1)
            cursor.close()

        elif change_part == 2:
            new_id = int(input("Enter new id: "))
            cursor.execute(f"UPDATE Product set id = {new_id} WHERE   id = {id}")
            print ("Total number of rows updated :", cursor.rowcount)
            connection.commit()
            print(Fore.GREEN, "id changed successfully")
            time.sleep(1)
            cursor.close()

        elif change_part == 3:
            new_price = int(input("Enter new price: "))
            cursor.execute(f"UPDATE Product set price = {new_price} WHERE   id = {id}")
            print ("Total number of rows updated :", cursor.rowcount)
            connection.commit()
            print(Fore.GREEN, "price changed successfully")

# exit from program   
    if User_selection == 6:
        print(Fore.BLUE , "Have a Great Day")
        time.sleep(3)
        break
    cursor.close()






















































































































