# __Python3 Cheat sheet__

# Variables & Stringes

Variables are used to store values. A string is a series of
characters, surrounded by single or double quotes.

## Hello world
```py
print("Hello world!")
```

## Hello world with a variable
```py
msg = "Hello world!"
print(msg)
```
## Concatenation (combining strings)
```py
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)
```

# Lists
>  list stores a series of items in a particular order. You
access items using an index, or within a loop.

A list stores a series of items in a particular order.
Lists allow you to store sets of information in one
place, whether you have just a few items or millions
of items. Lists are one of Python's most powerful
features readily accessible to new programmers, and
they tie together many important concepts in
programming.

## Make a list
```py
bikes = ['trek', 'redline', 'giant']
```

## List:Accessing elements
> Individual elements in a list are accessed according to their
position, called the index. The index of the first element is
0, the index of the second element is 1, and so forth.
Negative indices refer to items at the end of the list. To get
a particular element, write the name of the list and then the
index of the element in square brackets.

### Get the first item in a list
```py
first_bike = bikes[0]
```
### Get the last item in a list
```py
last_bike = bikes[-1]
```
### Looping through a list
```py
for bike in bikes:
    print(bike)
 ```


## List: Modifying individual Items
> Once you've defined a list, you can change individual
elements in the list. You do this by referring to the index of
the item you want to modify.

### Changing an element
```py
users[0] = 'valerie'
users[-2] = 'ronald'
```

## Adding elements
> You can add elements to the end of a list, or you can insert
them wherever you like in a list.

### Adding an element to the end of the list
```py
users.append('amy')
```
### Starting with an empty list
```py
users = []
users.append('val')
users.append('bob')
users.append('mia')
```
### Inserting elements at a particular position
```py
users.insert(0, 'joe')
users.insert(3, 'bea')
```

## Removing elements
> You can remove elements by their position in a list, or by
the value of the item. If you remove an item by its value,
Python removes only the first item that has that value

### Deleting an element by its position
```py
del users[-1]
```
### Removing an item by its value
```py
users.remove('mia')
```

## Popping elements
> If you want to work with an element that you're removing
from the list, you can "pop" the element. If you think of the
list as a stack of items, pop() takes an item off the top of the
stack. By default pop() returns the last element in the list,
but you can also pop elements from any position in the list.


### Pop the last item from a list
```py
most_recent_user = users.pop()
print(most_recent_user)
```


### Pop the first item in a list
```py
first_user = users.pop(0)
print(first_user)
```

## List Length
> The len() function returns the number of items in a list.
### Find the length of a list
```py
num_users = len(users)
print("We have " + str(num_users) + " users.")
```

## sorting a list
> The sort() method changes the order of a list permanently.
The sorted() function returns a copy of the list, leaving the
original list unchanged. You can sort the items in a list in
alphabetical order, or reverse alphabetical order. You can
also reverse the original order of the list. Keep in mind that
lowercase and uppercase letters may affect the sort order.

### Sorting a list permanently
```py
users.sort()
```
### Sorting a list permanently in reverse alphabetical order
```py
users.sort(reverse=True)
```
### Sorting a list temporarily
```py
print(sorted(users))
print(sorted(users, reverse=True))
```
### Reversing the order of a list
```py
users.reverse()
```

## Looping through a list
Lists can contain millions of items, so Python provides an
efficient way to loop through all the items in a list. When
you set up a loop, Python pulls each item from the list one
at a time and stores it in a temporary variable, which you
provide a name for. This name should be the singular
version of the list name.
 The indented block of code makes up the body of the
loop, where you can work with each individual item. Any
lines that are not indented run after the loop is completed.

### Printing all items in a list
```py
for user in users:
    print(user)
```
### Printing a message for each item, and a separate message afterwards
```py
for user in users:
    print("Welcome, " + user + "!")

print("Welcome, we're glad to see you all!")
```

## The `range()` function
You can use the range() function to work with a set of
numbers efficiently. The range() function starts at 0 by
default, and stops one number below the number passed to
it. You can use the list() function to efficiently generate a
large list of numbers.

### Printing the numbers 0 to 1000
```py
for number in range(1001):
    print(number)
```
## Printing the numbers 1 to 1000
```py
for number in range(1, 1001):
    print(number)
```
## Making a list of numbers from 1 to a million
```py
numbers = list(range(1, 1000001))
```

## Statistics
> There are a number of simple statistics you can run on a list
containing numerical data.
### Finding the minimum value in a list
```py
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
```
### Finding the maximum value
```py
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)
```
### Finding the sum of all values
```py
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)
```


## Slicing a list
> You can work with any set of elements from a list. A portion
of a list is called a slice. To slice a list start with the index of
the first item you want, then add a colon and the index after
the last item you want. Leave off the first index to start at
the beginning of the list, and leave off the last index to slice
through the end of the list.

### Getting the first three items
```py
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]
```
### Getting the middle three items
```py
middle_three = finishers[1:4]
```
### Getting the last three items
```py
last_three = finishers[-3:]
```




## Copying a list
To copy a list make a slice that starts at the first item and
ends at the last item. If you try to copy a list without using
this approach, whatever you do to the copied list will affect
the original list as well.
### Making a copy of a list
```py
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]
```

## List Comprehensions
You can use a loop to generate a list based on a range of
numbers or on another list. This is a common operation, so
Python offers a more efficient way to do it. List
comprehensions may look complicated at first; if so, use the
for loop approach until you're ready to start using
comprehensions.
 To write a comprehension, define an expression for the
values you want to store in the list. Then write a for loop to
generate input values needed to make the list.
### Using a loop to generate a list of square numbers
```py
squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)
```
### Using a comprehension to generate a list of square numbers
```py
squares = [x**2 for x in range(1, 11)]
```
### Using a loop to convert a list of names to upper case
```py
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
 upper_names.append(name.upper())
```
### Using a comprehension to convert a list of names to upper case
```py
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]
```





# Tuples
> Tuples are similar to lists, but the items in a tuple can't be
modified.
A tuple is like a list, except you can't change the values in a
tuple once it's defined. Tuples are good for storing
information that shouldn't be changed throughout the life of
a program. Tuples are designated by parentheses instead
of square brackets. (You can overwrite an entire tuple, but
you can't change the individual elements in a tuple.)

### Defining a tuple
```py
dimensions = (800, 600)
```
### Looping through a tuple
```py
for dimension in dimensions:
    print(dimension)
```
### Overwriting a tuple
```py
dimensions = (800, 600)
print(dimensions)
dimensions = (1200, 900)
```



# If statements
If statements are used to test for particular conditions and
respond appropriately.
## Conditional tests
```py
equals x == 42
not equal x != 42
greater than x > 42 or equal to x >= 42
less than x < 42 or equal to x <= 42
 ```
## Conditional test with lists
```py
'trek' in bikes
'surly' not in bikes
```
## Assigning boolean values
```py
game_active = True
can_edit = False
```
## A simple if test
```py
if age >= 18:
 print("You can vote!")
 ```
## If-elif-else statements
```py
if age < 4:
 ticket_price = 0
elif age < 18:
 ticket_price = 10
else:
 ticket_price = 15
```

## Testing if a value is not in a list
```py
banned_users = ['ann', 'chad', 'dee']
user = 'erin'
if user not in banned_users:
    print("You can play!")
```
## Checking if a list is empty
```py
players = []
if players:
 for player in players:
 print("Player: " + player.title())
else:
    print("We have no players yet!")
```






# Dictionaries
Dictionaries store connections between pieces of information. Each item in a dictionary is a key-value pair.

## A simple dictionary
```py
alien = {'color': 'green', 'points': 5}
```

## Accessing a value
```py
print("The alien's color is " + alien['color'])
```
## Adding a new key-value pair
```py
alien['x_position'] = 0
```


## Getting the value with get()
```py
alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
print(alien_color)
print(alien_points)
```

## Adding to an empty dictionary
```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
```

## Modifying values in a dictionary
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# Change the alien's color and point value.
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)
```

## Deleting a key-value pair
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

## Looping through all key-value pairs
```py
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
 print(name + ' loves ' + str(number))
 ```
## Looping through all keys
```py
fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
 print(name + ' loves a number')
```
## Looping through all the values
```py
fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
 print(str(number) + ' is a favorite')
```

## Looping through all the keys in order
```py
# Show each person's favorite language,
# in order by the person's name.
for name in sorted(fav_languages.keys()):
    print(name + ": " + language
```

## Finding a dictionary's length
```py
num_responses = len(fav_languages)
```

## Storing dictionaries in a list
```py
# Start with an empty list.
users = []
# Make a new user, and add them to the list.
new_user = {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 }
users.append(new_user)
# Make another new user, and add them as well.
new_user = {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 }
users.append(new_user)
# Show all information about each user.
for user_dict in users:
 for k, v in user_dict.items():
 print(k + ": " + v)
 print("\n")
```

## define a list of dictionaries directly
```py
# Define a list of users, where each user
# is represented by a dictionary.
users = [
 {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 },
 {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 },
]
# Show all information about each user.
for user_dict in users:
 for k, v in user_dict.items():
 print(k + ": " + v)
 print("\n")

```

## Storing lists in a dictionary
```py
# Store multiple languages for each person.
fav_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}
# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)
``` 

## Storing dictionaries in a dictionary
```py
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
 }
 
for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
```

## Preserving the order of keys and values
```py
from collections import OrderedDict

# Store each person's languages, keeping
# track of who respoded first.
fav_languages = OrderedDict()

fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

# Display the results, in the same order they were entered.
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
    print("- " + lang)
```

## Million dictionary
```py
aliens = []
# Make a million green aliens, worth 5 points
# each. Have them all start in one row.
for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)

# Prove the list contains a million aliens.
num_aliens = len(aliens)

print("Number of aliens created:")
print(num_aliens)
```


# User Input
Your programs can prompt the user for input. All input is
stored as a string.
## Prompting for a value
```py
name = input("What's your name? ")
print("Hello, " + name + "!")
```
## Prompting for numerical input
```py
age = input("How old are you? ")
age = int(age)
pi = input("What's the value of pi? ")
pi = float(pi)
```

# While loops
A while loop repeats a block of code as long as a certain
condition is true.
## A simple while loop
```py
current_value = 1
while current_value <= 5:
 print(current_value)
 current_value += 1
```
## Letting the user choose when to quit
```py
msg = ''
while msg != 'quit':
 msg = input("What's your message? ")
 print(msg)
```

## Using a flag
```py
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
    active = False
    else:
    print(message)
```

## Using break to exit a loop
```py
prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done. "
while True:
    city = input(prompt)
    if city == 'quit':
    break
    else:
    print("I've been to " + city + "!")
```

## Using continue in a loop
```py
banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)
```




# Functions
Functions are named blocks of code, designed to do one
specific job. Information passed to a function is called an
argument, and information received by a function is called a
parameter.
## A simple function
```py
def greet_user():
 """Display a simple greeting."""
 print("Hello!")
greet_user()
```
## Passing an argument
```py
def greet_user(username):
 """Display a personalized greeting."""
 print("Hello, " + username + "!")
greet_user('jesse')
```
## Using keyword arguments
```py
def describe_pet(animal, name):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")

describe_pet(animal='hamster', name='harry')
describe_pet(name='willie', animal='dog')
```

## Default values for parameters
```py
def make_pizza(topping='bacon'):
 """Make a single-topping pizza."""
 print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')
```

## Using Optional arguments for parameters
```py
def describe_pet(animal, name=None):
 """Display information about a pet."""
 print("\nI have a " + animal + ".")
 if name:
 print("Its name is " + name + ".")
describe_pet('hamster', 'harry')
describe_pet('snake')
```


## Returning a value
```py
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add_numbers(3, 5)
print(sum) 
```

## Collecting an arbitrary number of arguments
```py
def make_pizza(size, *toppings):
    """Make a pizza."""

    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

# Make three pizzas with different toppings.
make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers','onions', 'extra cheese')
```
## Collecting an arbitrary number of keyword arguments
```py
def build_profile(first, last, **user_info):
    """Build a user's profile dictionary."""

    # Build a dict with the required keys.
    profile = {'first': first, 'last': last}

    # Add any other keys and values.
    for key, value in user_info.items():
        profile[key] = value

    return profile

# Create two users with different kinds of information.
user_0 = build_profile('albert', 'einstein', location='princeton')
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry')

print(user_0)
print(user_1)
```

# Modules
You can store your functions in a separate file called a
module, and then import the functions you need into the file
containing your main program. This allows for cleaner
program files.

> Make sure your module is stored in the same directory as your main program.

## Storing a function in a module
```py
def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)
```

## Importing an entire module
Every function in the module is available in the program file.
```py
import pizza

pizza.make_pizza('medium', 'pepperoni')
pizza.make_pizza('small', 'bacon', 'pineapple')
```

## Importing a specific function
> Only the imported functions are available in the program file.
```py
from pizza import make_pizza

make_pizza('medium', 'pepperoni')
make_pizza('small', 'bacon', 'pineapple')
```

## Giving a module an alias
```py
import pizza as p

p.make_pizza('medium', 'pepperoni')
p.make_pizza('small', 'bacon', 'pineapple')
```

## Giving a function an alias
```py
from pizza import make_pizza as mp

mp('medium', 'pepperoni')
mp('small', 'bacon', 'pineapple')
```

## Importing all functions from a module
> Don't do this, but recognize it when you see it in others' code. It can result in naming conflicts, which can cause errors.
```py
from pizza import *

make_pizza('medium', 'pepperoni')
make_pizza('small', 'bacon', 'pineapple')
```


# Classes
A class defines the behavior of an object and the kind of
information an object can store. The information in a class
is stored in attributes, and functions that belong to a class
are called methods. A child class inherits the attributes and
methods from its parent class.
## Creating a dog class
```py
class Dog():
 """Represent a dog."""
 def __init__(self, name):
 """Initialize dog object."""
 self.name = name
 def sit(self):
 """Simulate sitting."""
 print(self.name + " is sitting.")
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()
```



# Inheritance
```py
class SARDog(Dog):
    """Represent a search dog."""

    def __init__(self, name):
        """Initialize the sardog."""
        super().__init__(name)

    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")

my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
```

# Working with files
Your programs can read from files and write to files. Files
are opened in read mode ('r') by default, but can also be
opened in write mode ('w') and append mode ('a').

## Reading an entire file at once
```py
filename = 'eeert.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)
```
## Reading line by line
```py
filename = 'myfile.txt'
with open(filename) as f_obj:
    for line in f_obj:
    print(line.rstrip())
```


## Reading a file and storing its lines
```py
filename = 'killercodes.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)
```

## Writing to a file
```py
filename = 'journal.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.")
```

## Appending to a file
```py
filename = 'journal.txt'
with open(filename, 'a') as file_object:
 file_object.write("\nI love making games.")
```



# Exception
Exceptions help you respond appropriately to errors that
are likely to occur. You place code that might cause an
error in the try block. Code that should run in response to
an error goes in the except block. Code that should run only
if the try block was successful goes in the else block.

## Catching an exception
```py
prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
 num_tickets = int(num_tickets)
except ValueError:
 print("Please try again.")
else:
 print("Your tickets are printing.")
```

## Handling the FileNotFoundError exception
```py
f_name = 'myfile.txt'

try:
    with open(f_name) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "Can't find file {0}.".format(f_name)
    print(msg)
```

## Using an else block
```py
print("Enter two numbers. I'll divide them.")
x = input("First number: ")
y = input("Second number: ")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(result)
```

## Using the pass statement in an else block
```py
f_names = ['alice.txt', 'area51.txt','moby_dick.txt', 'little_women.txt']
for f_name in f_names:
    # Report the length of each file found.
    try:
        with open(f_name) as f_obj:
        lines = f_obj.readlines()
    except FileNotFoundError:
        # Just move on to the next file.
        pass
    else:
        num_lines = len(lines)
        msg = "{0} has {1} lines.".format(f_name, num_lines)
        print(msg)
```
> Exception-handling code should catch specific exceptions
that you expect to happen during your program's execution.
A bare except block will catch all exceptions, including
keyboard interrupts and system exits you might need when
forcing a program to close.

## Don’t use bare except blocks
```py
try:
    # Do something
except:
    pass
```
## Use Exception instead
```py
try:
    # Do something
except Exception:
    pass
```
## Printing the exception
```py
try:
    # Do something
except Exception as e:
    print(e, type(e))
```

# JSON File
> The json module allows you to dump simple Python data
structures into a file, and load the data from that file the
next time the program runs. The JSON data format is not
specific to Python, so you can share this kind of data with
people who work in other languages as well

## Using json.dump() to store data
```py
"""Store some numbers."""

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```
## Using json.load() to read data
```py
"""Load some previously stored numbers."""
import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
```
## Making sure the stored data exists
```py
import json

f_name = 'numbers.json'

try:
    with open(f_name) as f_obj:
    numbers = json.load(f_obj)
except FileNotFoundError:
    msg = "Can’t find {0}.".format(f_name)
    print(msg)
else:
    print(numbers)
```


---
