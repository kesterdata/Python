#Python Functions

"""A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

"""

#Example
"""
def mysum():
    print("The value of pi constant is  3.14156")

mysum()
mysum()
mysum()
"""

#Example two: Calling functions inside a function.


"""def thankUser():
    print("Thanks for acceping the terms and condition")

def askUser():
    user_response = input("Do you accept out terms and condition (Y/N)? :")
    if user_response =="Y":
        thankUser()
    else:
        print("Have a good day")

askUser()"""

#Example 3: Calling functions inside a function using the Return

"""def thankUser():
    return "Thank you for accepting the terms and condition"

def askquestions():
    questions = input("Are you male or Female (M/F) : " )
    if questions =="M":
        message = thankUser()
        print(message)
    else:
        questions =="F"
        print("Females are not allowed")

askquestions()"""

#CLASS EXERCISE :
"""
Create a function checkPassword that askes a user to enter a password.
if the password is equal to gomycode, it should call the function 'correct_password'
That prints 'pass is correct'. Elee if the password is wrong it should call another function 'wrong_password'
which prints 'You have enter a wrong password'
"""

"""def correct_password():
    print("Password is correct")

def wrong_password():
    print("You have entered a wrong password")

def checkPassword():
    enter_password = input("Enter password : ")
    if enter_password =="gomycode":
       correct_password()
    else:
            wrong_password()
checkPassword()"""



"""Arguments and Parameters

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")"""

"""The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
"""

"""def sum_two_numbers(a,b):
    print(a+b)

sum_two_numbers(2,5)"""

"""#EXCERCISE 
def print_area(b,h):
    result = (b*h)/2
    return result
    
area = print_area(3,4)

print(f"Triangle area :{area}")"""

"""#RETURN STATEMENTS

def minimum_number(a,b):
    if a>b:
        return b 
    else:
        return a
print(minimum_number(3,5))"""


"""def print_scores(scores,bonus):
    for score in scores:
        print(f"{score} would be updated to {score+bonus}")
    
print_scores([67,68,72,71,69],10)"""

    
"""Write a function that would create a multiplication table for any number.
The function would take in a list of numbers at the first parameter called 'numbers'
and the 'multiplier' as the second parameter.



"""
"""def multi_table(numbers,multiplier):
    for number in numbers:
        print(f"{multiplier}* {number} = {number*multiplier}")
        

multi_table([1,2,3,4,5,6,7,8,9,10,11,12,13,14],4)"""





"""""practice = lambda x,y: x**y
print(practice(4,4))"""

"""list = [1,2,3,4,5,6,7,8,9,10,11,34,30,45]

listlamb = lambda x : x[-7::2]
print(listlamb(x=list))"""


"""print_area = lambda b,h : (b*h)/2
print(print_area(3,4))"""

lis =[45,56,79,102,23,45]

temperatures = list(map(lambda C: (9/5)*C + 32, lis))
print(temperatures)