
print("Welcome to Python Pizza Deliveries")
size = input("Choose your pizza size(S,M,L) : ")
add_pepperoni = input("Do you want pepperoni? (Y/N): ")
extra_cheese = input("Do you want extra cheese? (Y/N): ")

bill = 0  

if size == "S":  
    bill += 15  
    if add_pepperoni == "Y":  
        bill += 2  
elif size == "M":  
    bill += 20  
    if add_pepperoni == "Y":  
        bill += 3  
elif size == "L":  
    bill += 25  
    if add_pepperoni == "Y":  
        bill += 3  

if extra_cheese == "Y":  
    bill += 1

print(f"Your final bill is: ${bill}.")