"""def add(a,b):
    return a+b

def substraction(a,b):
    return a-b


operations = {"+" : add(), "-": substraction()}

def calculate():
    print("")
    for symbol in operations.keys():
        print(symbol)

calculate()"""



def add(c, d):  
    return c + d  

def subtract(c, d):  
    return c - d  

def multiply(c, d):  
    return c * d  

def divide(c, d):  
    if d != 0:  
        return c / d  
    else:  
        return "Error!."  

# Create a dictionary to store operations  
operations = {  
    '+': add,  
    '-': subtract,  
    '*': multiply,  
    '/': divide  
}  

# Calculator function  
def calculator():  
    num1 = float(input("Enter the first number: "))  
    should_continue = True  

    while should_continue:  
        # Print available operations  
        print("Select an operation:")  
        for operation in operations:  
            print(operation)  
        
        operation_symbol = input("Enter the operation: ")  
        
        if operation_symbol in operations:  
            num2 = float(input("Enter the second number: "))  
            calculation_function = operations[operation_symbol]  
            answer = calculation_function(num1, num2)  

            print(f"{num1} {operation_symbol} {num2} = {answer}")  

            # Ask the user if they want to continue with the result  
            continue_calculating = input("Do you want to continue calculating with this result? (yes/no): ").lower()  
            if continue_calculating == 'yes':  
                num1 = answer  
            else:  
                should_continue = False  
                calculator()  # Start new calculation  
        else:  
            print("Invalid operation. Please select a valid operation.")  

# Start the calculator  
calculator()
