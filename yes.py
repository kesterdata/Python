def add(num1, num2):  
    return num1 + num2  

def subtract(num1, num2):  
    return num1 - num2  

def multiply(num1, num2):  
    return num1 * num2  

def divide(num1, num2):  
    if num2 == 0:  
        return "Cannot divide by zero!"  
    return num1 / num2  

operations = {  
    '+': add,  
    '-': subtract,  
    '*': multiply,  
    '/': divide  
}  

def calculator():  
    num1 = float(input("Enter the first number: "))  
    
    while True:  
        for symbol in operations:  
            print(symbol)  
        
        operation_symbol = input("Select an operation: ")  
        num2 = float(input("Enter the second number: "))  
        
        calculation_function = operations[operation_symbol]  
        answer = calculation_function(num1, num2)  
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")  
        
        continue_calc = input("Do you want to continue with this result? (yes/no): ")  
        if continue_calc.lower() == 'yes':  
            num1 = answer  
        else:  
            break  

calculator()