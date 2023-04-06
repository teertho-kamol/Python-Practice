Name: Teertho Kamol Goshami Likhon

"""

print("Hello world")

"""Here, I print 'Hello world' using python print function."""

age = 23
weight = 72.5
name = "Teertho"
good_programmer = True

print(age)
print(weight)
print(name)

"""Here, I store data in variable age, weight, name, good_programmer and print all data."""

address = "Savar"
name = "Teertho"

print ("Teertho lives in savar")
print(name + " lives in "+ address)

"""This lesson, we input user data and print this."""

name = input("what is your name?")

"""Here, I learn how to put user input in variable and print."""

celsius = input("Temperature in Celsius")
celsius = int(celsius)
fahernheit = (celsius * (9/5)) + 32
print(fahernheit)

"""Here, I input a celcius data in celcius variable and convert it farhernheit and print."""

course_name = "Learn Python Programming"
print(course_name[3:-4])

"""Here, The notation [3:-4] is used to slice the string and includes all character from 3 """

name = 'Nuruzzaman Faruqui'
code_name = 'NF'
message = name + '(' + code_name + ') teaches AI'
print(message)
message_1 = f'{name}({code_name}) teaches AI'
print(message_1)

"""Here I concataning two string. To do that i can simply use + or using f format to acheive the same output."""

course_name = 'Learn Python Programming'
print(len(course_name))
print(course_name.upper())
print(course_name.lower())
print(course_name)
print(course_name.find('Python'))
print(course_name.replace('Learn', 'Master'))
print('learn' in course_name)

"""We used several build in string methods techniques."""

print(5-3)
print(5+3)
print(5*3)
print(5/3)
print(5//3)
print(5%3)
print(5**3)

x = 5
x = x + 5
x += 5
print(x)


y = 5
y -= 2
print(y)

z = 5 + 3 * 2 ** 2
print(z)

p = (5+3) * 2 ** 2
print(p)

q = (1+2) * (5-3)
print(q)

"""Here I learn logical operator using python."""

import math

print(math.ceil(5.7))
print(math.floor(5.7))
print(math.factorial(5))
x = 5.7
print(round(x))
print(abs(-5.7))

"""Here, I import math.py module and uses some of function to perform operation on numbers."""

is_rainy = True
is_sunny = False

if is_rainy:
  print("Carry an umbrella")
elif is_sunny:
  print("No need to carry an umbrella")   
else:
  print("Check the weather")

"""Here I compare two boolean variable is_rainy and is_sunny using if-elif-else condition to determine the result."""

good_condition = True
reasonable_value = False
poor_foundation = False

if good_condition and reasonable_value:
  print("We will buy the house")

if good_condition and reasonable_value:
  print("We are interested")

if good_condition and not poor_foundation:
  print("It is a good deal")

"""Here i learn conditional statements to check three boolean value and print the statement."""

price = 10

if price ==10:
  print("We will buy it")

if price != 10:
  print("The price is not 10")

if price > 10:
  print("The price is more than 10")

"""Here I store 10 in price variable and a series of conditional statements to print value."""



actual_price = 10
guess_count = 0
guess_limit = 5

while guess_count < guess_limit:
  guess = int(input("Guess the price: "))
  guess_count += 1

  if guess == actual_price:
    print("You've won the game")
    break
else:
    print("You failed")

"""Here i create a while loop to allow user to guess the value price, and also create else block when if condition faild then "You Faild" message show."""

for character in 'Python':
    print(character)

for item in ['Egg', 'Milk', 'Rice']:
    print(item)

for number in [1, 2, 3, 4]:
    print(number)

for x in range(10):
    print(x)

for y in range(5, 10):
    print(y)

for z in range(5, 10, 2):
    print(z)

bills = [10, 20, 30]
total = 0

for bill in bills:
    total += bill
print(f"Total bill: ${total}")

"""Here we see the seven total for loops, the loops using diffent types of objects. The last for loops we see to iterate over a list of number and print the total."""

for x in range(1, 10):
  print(x)

"""Here we see the for loop and range function how to calculate the total."""

for x in range(4):
  for y in range(4):
    print(f"{x},{y}")

"""Here i learn nested loop how to work. for is a loop and then for loop is a nested. here x and y that range is 0 to 3."""

grocery_list = ['egg', 'rice', 'bread', 'sugar']
grocery_list[1] = 'oil'
print(grocery_list[1:2])
print(grocery_list)

price = [5, 10, 15, 1, 3, 7]
max = price[0]
for value in price:
    if value > max:
        max = value
print(max)

"""Here i create array list to store different product.Then entered the value oil in the grocery_list[1] then sliced the value after that we find out the max value in the array list. """

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0][2])
matrix[0][2] = 15
print(matrix)

for row in matrix:
    for item in row:
        print(item)

"""Here i learn two dimensional list or matrix. That contains three rows and three columns of integer values."""

number_list = [1, 2, 5, 1, 10, 14]
number_list.append(20)
number_list.insert(1, 7)
number_list.remove(2)
number_list.sort()
number_list.reverse()
print(number_list)
print(12 in number_list)
print(number_list.count(1))
print(number_list.index(10))
number_list.pop()
number_list_2 = number_list.copy()
number_list_2.clear()
print(number_list_2)

"""Here we can see the some of lists like append(), insert(), remove(), sort() and pop() etc."""

number_list = [1, 2, 1, 5, 6, 5, 10]
unique = []

for number in number_list:
    if number not in unique:
        unique.append(number)
print(unique)

"""Here we see the two array list number_list and unique. Then the for loop oparation the number_list data if the number was unique then print in unique value."""

number_tuple = (1, 2, 3)
number_tuple[1] = 10
print(number_tuple)
print(number_tuple[1])

"""Here i start learn tuple how to work in python. But there is a type error shown the compiler. Tuple in python are immutable, their values changed after they are created. """

number_tuple = [1, 2, 3]
add_num_tuple = number_tuple[0] + number_tuple[1] + number_tuple[2]
print(add_num_tuple)

x = number_tuple[0]
y = number_tuple[1]
z = number_tuple[2]
print(x + y + z)

a, b, c = number_tuple
print(a + b + c)

"""We create a tuple number_tuple. And insert value. And the add_num_tuple we add all. Then print the value."""

user = {
    "Name": "Nuruzzaman Faruqui",
    "Age": 28,
    "Email": "faruquizaman27@gmail.com",
    "is_Verified": True
}
user["Age"] = 29
user["Job"] = "Teaching"
print(user)

"""Here we learn how to use dictionary in python. And how to access the properties of dictionary."""

message = input("Type your message: ")
separate_words = message.split(' ')
print(separate_words)

emoji = {
    ":)": "😊",
    ":(": "☹"
}
output = ""
for word in separate_words:
    output += emoji.get(word, word) + " "
print(output)

"""Here we create dictionary emoji, and my text replaced according to the values of them."""

def total_cost(price, shipping, discount):
    print(f"Total cost: ${price + shipping - discount}")


total_cost(shipping=5, discount=1, price=10)


def welcome(fist_name, last_name):
    print(f"Hi {fist_name} {last_name}")


welcome("Nuruzzaman", "Faruqui")

"""Here I learn how to create a function. def total_cost is a function i create. And print Total cost."""

def add(number_1, number_2):
    return number_1 + number_2


print(add(1, 2))

"""Here i def add and return summation result."""

def emoji_converted(message):
    separate_words = message.split(' ')
    emoji = {
        ":)": "😊",
        ":(": "☹"
    }
    output = ""
    for word in separate_words:
        output += emoji.get(word, word) + " "
    return output


message = input("Type your message: ")
result = emoji_converted(message)
print(result)

"""This lesson i learn how to used function to make our code reuseable. """

try:
    celsius = int(input("Temperature  in Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    print(fahrenheit)
    print(f"F to C ratio (F/C): {fahrenheit/celsius}")
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Celsius cannot be 0')

"""Here we handle the exception handiling for the unwanted inputs. If the user invalid input or something error then ValueError exception will be show, else if then 0."""

# Welcome Message
# It prints Hi! How are you doing
print("Hi! How are you doing?")


# It sum num1 and num2 and return the output
def add(num1, num2):
    return num1 + num2

'''
Sometimes we need a
multiline comment
'''

"""
This is also a
multiline comment
"""

"""Here i learn how to use single line #message and ""multiline"" comment in python."""

class Keyboard:
    def definition(self):
        print("Keyboard is an input device")

    def number_of_keys(self):
        print('There are 101 keys')


my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.number_of_keys()
my_keyboard.brand = "Logitech"
print(my_keyboard.brand)

new_keyboard = Keyboard()
new_keyboard.definition()
new_keyboard.brand = "Dell"
print(new_keyboard.brand)

"""Here we can create class and object. Here we created a class named keyboard and added two methods within it named defination and number_of_keys. From this class we have created an object named my_kyboard. And inserted value in the object's properties."""

class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

    def definition(self):
        print("Keyboard is an input device")

    def numer_of_keys(self):
        print("There are 101 keys")


my_keyboard = Keyboard('English', 'wireless')
print(my_keyboard.connection)


class AboutMe:
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    def talk(self):
        print(f"My name is {self.name}. I am from {self.address}. And "
              f"I am a {self.occupation}")


faruqui = AboutMe('Nuruzzaman Faruqui', 'Bangladesh', 'teacher')
faruqui.talk()

russel = AboutMe('David Russel', 'UK', 'Web Developer')
russel.talk()

"""Here we learn and use the consturctor function in python. Instantiate our values to it's attributes instead of direct insertion like we did in the previous lesson. And used the methods to print the result."""

class Laptop:
    def parts(self):
        print('Keyboard, Display, Motherboard')


my_laptop = Laptop()
my_laptop.parts()


class Desktop(Laptop):
    def weight(self):
        print('Desktops are heavy-weight')

my_desktop = Desktop()
my_desktop.parts()
my_desktop.weight()

"""Here the Laptop class and parts is a function that simply prints the parts. The Desktop class inherits the Laptop class. The code creats an instance of my_laptop and calls the parts method on it and print the parts of a laptop. Otherwise, The my_desktop inherited from the Laptop class and print. """

import our_module
from our_module import find_max

our_module.lower_case('HELLO PYTHON')
our_module.upper_case('hello python')
result = find_max([1, 120, 500, 10])
print(result)

"""Here we learn how to import a file and how to another file using import file."""

from our_package import number_module
from our_package import string_module

string_module.upper_case('hello python')

result = number_module.find_max([1, 5, 10, 12])
print(result)

"""Here we used third-party libraries to do our job. upper_case and find_max function is simply import and ready to use in python."""

import random

for i in range(5):
    print(random.randint(5, 10))

member_list = ['A', 'B', 'C', 'D', 'E']
member = random.choice(member_list)
print(member)

"""Here we import random package and we can get random number value or character value from character list."""

from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)

"""Here we learn how to import dictionary in python and how to use it. The dictionary file extention is .py and printing the path of each file to the console."""