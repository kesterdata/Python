"""
A loop is a code construct that runs a set of statement while a condition is true. 
In python there are two types of loops which are

1. While loop and 
2. For loop

"""
"""
n = 1

while n <=10:
    print(f"n is at {n} now")
    n = n+1
   """ 

    
    
    
"""n = 5
while n >=1:
    print(f"y is at {n}")
    n = n - 1 """

"""
n = 10
while n >=5:
  print(f"{n}")
  n = n - 1
"""


"""6guessed_password = ""
while guessed_password != "hacker":
    guessed_password = input("Enter correct password")
    print("Wrong passord! Try again")
print("Passord correct") """

#ASSIGNMENT
#Use a while loop to write a code that wil ask a user to guess an answer to a quiz question.
"""print("Quiz Questions")
answer = ""
while answer != "64":
    answer = input("How old is Nigeria ")
    print("Incorrect! Give it another try")
print("Correct!") """


""" 
The break Statement
With the break statement we can stop the loop even if the while condition is true:
""" 
#Example
#Exit the loop when i is 3:
"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  

The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  """

  #Example 2

"""
while true:
     answer = input("Enter the correct answer")
     if answer == "stop":
        print("You have stopped the program")
        break
"""         
"""    
print ("Quiz Questions")
while True:
    answer = int(input("How old is Nigeria"))
    if answer == 64:
        print("Correct!")
        break
    else:
        print("Your answer is wrong")
""" 

""" 
trails =1
while True:
    trails +=1
    password = input("Enter the correct answer: ")
    if password == "stop" and trails <=5:
        print("You guessed the passord. ")
        break
    elif  password != "stop" and trails <=5:
        print("wrong password! try again")
    else:
        print("Max trails reached. Try again after 30 minutes")
        break
    """ 

"""Write a programm that allows a user to guess a magic number and they have only three attempts to guess the correct magic nummber
    he magic number is 7. 
 1.if the user guesses the number and do not exhaust his trials print congratulations and stop the programm.
2. if the user guesses wrong and do not exhaust his or her trial print " wrong guess try again.
3. After 3 failed attempts print "Sorry you have exhausted your trail, The magic number was. 
after each wrong guess, give them a clue if their guess is higher or greater than the magic number.
"""

trails = 0
while True:
    trails = trails + 1
    magic_number =int(input("Guess the number : "))
    if magic_number == 7 and trails <=3:
        print("Congratulations ")
        break
    elif magic_number != 7 and trails <3:
        if magic_number > 7:
         print("Wrong guess! Try again Your input is too high")
        else:
           print("Wrong guess your number is too low! Try again")
    else:
        print("Sorry you have exhausted your trail. The magic number was 7")
        break
