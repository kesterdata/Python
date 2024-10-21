#bject-oriented programming (OOP) 

"""Object-oriented programming (OOP) in Python is a programming paradigm that organizes code by bundling related properties and behaviors into objects.

Objects bundles related attributes or properties (variable) and can perform  actions(behaviours) which are called methods in classes. 

Class Is used to design the structure

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""
"""#EXAMPLE 1 
#(CONSTUCTOR)
class Car:
    def __init__(self, brand,model,year,engine_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_type = engine_type

##ACTIONS  (METHODS)
    def start(self):
        print(f"{self.model} is starting")

    def stop_car(self):
        print(f"{self.model} stopped")
    def drive(self):
        print(f"{self.model} is ready to drive")

car1 = Car("Toyota","Camry","2010","V6")
car2 = Car("Toyota","Corolla",2010,"V6")




car1.stop_car()
car1.drive()
"""
"""print(car2.brand, car2.year, car2.engine_type)"""

"""#EXAMPLE 2
class Phone:
    def __init__(self, brand, year, operating_system, price):
        self.brand = brand
        self.year = year
        self.operating_system = operating_system
        self.price = price

phone1 = Phone("Iphone",2024,"IOS",1099)
phone2 = Phone("Samsung",2023,"Andriod",1000)

print(phone1.brand,phone1.year, phone1.operating_system,phone1.price)
print(phone2.brand,phone2.operating_system,phone2.year,phone2.price)
   """


"""class BankAccount:
    def __init__(self, owner,phone_number,email_address,account_number,balance=0):
        self.owner = owner
        self.phone_numer = phone_number
        self.email_address = email_address
        self.account_number = account_number
        self.balance = balance
        

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f" Alert!!! {self.owner} {deposit_amount} was credited to your account")

    def check_balance(self):
        print(f"Hi {self.owner} your balance is {self.balance}")
    
    def withdraw(self,withdrawal_amount):
        self.balance -= withdrawal_amount
        print(f" Debit Alert!!! {self.owner} {withdrawal_amount} was debited from your account")

    def account_info(self):
        print(f" This is your account details : \n Name:{self.owner} \n Phone: {self.phone_numer} \n Email: {self.email_address}\n Account Number :{self.account_number}\n Your balance is {self.balance} ")
        
    def update_email(self,new_email):
        old_email =self.email_address
        self.email_address = new_email
        print(f"Your email {old_email} has been updated to {new_email}")

account1 = BankAccount("Kester","08127610040","kester2023@gmail.com", "99338492103")
print(f"Good afternoon {account1.owner}, your account is {account1.account_number}")

account1.deposit(10)
account1.deposit(50)
account1.deposit(60)
account1.check_balance()
account1.withdraw(50)
account1.check_balance()
account1.account_info()
account1.update_email("kester0000@gmail.com")"""


"""class Player:
    def __init__(self,name,hp=100):
        self.name = name
        self.hp = hp

    def run(self):
        print(f"{self.name} is running in the game")

    def take_damage(self,damage):
       
        self.hp -= damage
        print(f"{self.name} your hit points is {self.hp} ")

        if self.hp <50:
            print(f"{self.name} you are at the verge to death")

        elif self.hp >= 80:
            boost_num = 20
            boost = self.hp + boost_num
            print(f"{self.name} received a {boost_num} boost and your total point is {boost}")


        
player_one = Player("Harry Potter")
player_two = Player("Kester")
player_three = Player("John")
player_one.take_damage(10)
player_two.take_damage(60)
player_three.take_damage(50)"""






    

