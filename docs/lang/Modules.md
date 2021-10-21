# Modules
A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

> A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

Example
The Python code for a module named aname normally resides in a file namedaname.py. Here is an example of a simple module, support.py −
```python
# A simple module, support.py
  
def add(x, y):
    return (x+y)
  
def subtract(x, y):
    return (x-y)
    
def print_func( par ):
   print("Hello : ", par)
   return
```   
## The import Statement
We can import the functions, classes defined in a module to another module using the import statement in some other Python source file. You can use any Python source file as a module by executing an import statement in some other Python source file. The import has the following syntax −

```
import module1[, module2[,... moduleN]
```
When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches before importing a module. For example, to import the module hello.py, you need to put the following command at the top of the script −

> **Note:** This does not import the functions or classes directly instead imports the module only. To access the functions inside the module the dot(.) operator is used.

```python
#!/usr/bin/python3

# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Zara")
```
When the above code is executed, it produces the following result −
```
Hello : Zara
```
 A module is loaded only once, regardless of the number of times it is imported. This prevents the module execution from happening repeatedly, if multiple imports occur.

## The from...import Statement
Python's from statement lets you import specific attributes from a module into the current namespace. Python’s from statement lets you import specific attributes from a module without importing the module as a whole.
The from...import has the following syntax −
```
from modname import name1[, name2[, ... nameN]]
```
For example, to import the function fibonacci from the module fib, use the following statement −
```python
#!/usr/bin/python3

# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
>>> from fib import fib
>>> fib(100)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
This statement does not import the entire module fib into the current namespace; it just introduces the item fibonacci from the module fib into the global symbol table of the importing module.
```
The from...import * Statement
```
It is also possible to import all the names from a module into the current namespace by using the following import statement −
```
from modname import *
```
This provides an easy way to import all the items from a module into the current namespace; however, this statement should be used sparingly.

## Import all Names – From import *  Statement

The * symbol used with the from import statement is used to import all the names from a module to a current namespace.

Syntax:
```
from module_name import *
```
The use of * has its advantages and disadvantages. If you know exactly what you will be needing from the module, it is not recommended to use *, else do so.

Example: Importing all names
```py
# importing sqrt() and factorial from the
# module math
from math import *
  
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))
```
Output
```
4.0
720
```


## Executing Modules as Scripts
Within a module, the module’s name (as a string) is available as the value of the global variable __name__. The code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".

Add this code at the end of your module −
```python
#!/usr/bin/python3

# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fib(100)
   print(f)
```   
When you run the above code, the following output will be displayed.
```
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
## Locating Modules
When you import a module, the Python interpreter searches for the module in the following sequences −

- The current directory.
- If the module is not found, Python then searches each directory in the shell variable PYTHONPATH.
- If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python3/.

The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.

```py
Example: Directories List for Modules
Python3

# importing sys module
import sys
  
# importing sys.path
print(sys.path)
```

## Importing and renaming module
We can rename the module while importing it using the as keyword. 

Example: Renaming the module
```py

# importing sqrt() and factorial from the
# module math
import math as gfg
  
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(gfg.sqrt(16))
print(gfg.factorial(6))
```
Output
```
4.0
720
```

## The dir() function
The dir() built-in function returns a sorted list of strings containing the names defined by a module. The list contains the names of all the modules, variables, and functions that are defined in a module.

```py
#  Import built-in module  random
import  random
print(dir(random))
```

## Code Snippet illustrating python built-in modules: 

```py
# importing built-in module math
import math
  
# using square root(sqrt) function contained 
# in math module
print(math.sqrt(25)) 
  
# using pi function contained in math module
print(math.pi) 
  
# 2 radians = 114.59 degrees
print(math.degrees(2))  
  
# 60 degrees = 1.04 radians
print(math.radians(60))  
  
# Sine of 2 radians
print(math.sin(2))  
  
# Cosine of 0.5 radians
print(math.cos(0.5))  
  
# Tangent of 0.23 radians
print(math.tan(0.23)) 
  
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))  
  
# importing built in module random
import random
  
# printing random integer between 0 and 5
print(random.randint(0, 5))  
  
# print random floating point number between 0 and 1
print(random.random())  
  
# random number between 0 and 100
print(random.random() * 100)  
  
List = [1, 4, True, 800, "python", 27, "hello"]
  
# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List)) 
  
  
# importing built in module datetime
import datetime
from datetime import date
import time
  
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())  
  
# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))  
```
