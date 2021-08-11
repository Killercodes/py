# Modules
A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

Example
The Python code for a module named aname normally resides in a file namedaname.py. Here is an example of a simple module, support.py −
```python
def print_func( par ):
   print "Hello : ", par
   return
```   
## The import Statement
You can use any Python source file as a module by executing an import statement in some other Python source file. The import has the following syntax −

```
import module1[, module2[,... moduleN]
```
When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches before importing a module. For example, to import the module hello.py, you need to put the following command at the top of the script −
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
Python's from statement lets you import specific attributes from a module into the current namespace. The from...import has the following syntax −
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
