"""shopping_items = []
for i in range(6):
    user_item = input("Enter item name")
    shopping_items.append(user_item)

for n in shopping_items:
    print(n)"""

#create a student info input where studends input their information and stop this inside a dictionary.

students_info = {}
questions = ["What's your name ","How old are you","What class are you?","Where are you from?","Enter your email address."]
keys =["name","age","class","state","email"]

size = len(questions)

for i in range(size):
    current_questions = (questions[i])
    user_response = input(current_questions)
    students_info[keys[i]] = user_response
print(students_info)

