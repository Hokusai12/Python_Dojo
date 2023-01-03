num1 = 42 #variable-declaration, initialize-integer
num2 = 2.3 #variable-declaration, initialize-float
boolean = True #variable-declaration, initialize-boolean
string = 'Hello World' #variable-declaration, initialize-string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list-initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary-initialization
fruit = ('blueberry', 'strawberry', 'banana') #tuple-initialization
print(type(fruit)) #log-statement, type-check
print(pizza_toppings[1]) #log-statement, list-access-value 
pizza_toppings.append('Mushrooms') #list-add-value
print(person['name']) #log-statement, dictionary-access-value
person['name'] = 'George' #dictionary-change-value
person['eye_color'] = 'blue' #dictionary-change-value
print(fruit[2]) #log-statement, tuple-access-value

if num1 > 45: #if
    print("It's greater") #log-statement
else: #else
    print("It's lower") #log-statement

if len(string) < 5: #if, length-check
    print("It's a short word!") #log-statement
elif len(string) > 15: #else if, length-check
    print("It's a long word!") #log-statement
else: #else
    print("Just right!") #log-statement

for x in range(5): #for-loop-start, for-loop-increment, for-loop-stop
    print(x) #log-statment
    
for x in range(2,5): #for-loop-start, for-loop-increment, for-loop-stop
    print(x) #log-statement
    
for x in range(2,10,3): #for-loop-start, for-loop-increment, for-loop-stop
    print(x) #log-statement

x = 0 #variable-declaration, integer-initialization
while(x < 5): #while-loop-start, while-loop-stop
    print(x) #log-statement
    x += 1 #while-loop-increment

pizza_toppings.pop() #list-delete-value
pizza_toppings.pop(1) #list-delete-value

print(person) #log-statement
person.pop('eye_color') #dictionary-delete-value
print(person) #log-statement

for topping in pizza_toppings: #for-loop-start, for-loop-increment, for-loop-stop
    if topping == 'Pepperoni': #if
        continue #for-loop-continue
    print('After 1st if statement') #log-statement
    if topping == 'Olives': #if
        break #for-loop-break

def print_hello_ten_times(): #function-declaration
    for num in range(10): #for-loop-start, for-loop-increment, for-loop-stop
        print('Hello') #log-statement

print_hello_ten_times() #function-call, function-argument

def print_hello_x_times(x): #function-declaration, function-parameter
    for num in range(x): #for-loop-start, for-loop-increment, for-loop-stop
        print('Hello') #log-statement

print_hello_x_times(4) #function-call, function-argument

def print_hello_x_or_ten_times(x = 10): #function-declaration, function-parameter
    for num in range(x): #for-loop-start, for-loop-increment, for-loop-stop
        print('Hello') #log-statement

print_hello_x_or_ten_times() #function-call
print_hello_x_or_ten_times(4) #function-call, function-argument


"""
Bonus section #multi-line-comment
"""

print(num3) #Error-NameError
num3 = 72 #variable-declaration, integer-initialization
fruit[0] = 'cranberry' #Error-tuple-change-value
print(person['favorite_team']) #Error-KeyError-'favorite_team'
print(pizza_toppings[7]) #Error-IndexError-list index is out of range
  print(boolean) #Error-IndentationError-Unexpected indentation
fruit.append('raspberry') #Error-tuple object has no attribute 'append'
fruit.pop(1) #Error-tuple object has no attribute 'pop'