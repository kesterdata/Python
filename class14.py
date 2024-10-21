"""import random
randcovert = random.randint(0,1)
if randcovert == 0:
    print("Heads")
else:
    print("Tails")"""


shopping_list = []
unique_items = set()
items_info = {}


while True:
    print("""Shopping List Menu
          1. Add Item
          2. Remove Item
          3. View Items
          4. Exit
          
          """)
    user_choice = int(input("Select from the available options(1/2/3/4): \n"))
    if user_choice ==1:
        print("Add Item Selected")
        for i in range(5):
            item = input("Enter item")
            if item in unique_items:
                print(f"{item} is already in shopping list")
            else:
                item_quantity = int(input(f"How many quantity of {item} ?"))
                shopping_list.append(item)
                unique_items.add(item)
                items_info[item] = item_quantity
                print(f"{item} has been added to your shopping cart")

    elif user_choice == 3:
        print("Displaying items in your cart")
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(f"{item} with {items_info[item]} quantity(s)")
        
        else:
            print("Your cart is empty")


    elif user_choice == 4:
        print("Thank you for patronizing us")
        break
    
    elif user_choice == 2:
        