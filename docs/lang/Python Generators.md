# Python Generators

There are two terms involved when we discuss generators.

## Generator-Function :

A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

```py
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)
```
Output :
```
1
2
3
```
## Generator-Object : 

Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).

```py
# A Python program to demonstrate use of 
# generator object with next() 
  
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
   
# x is a generator object
x = simpleGeneratorFun()
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
```

Output :
```
1
2
3
```
So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .

As another example, below is a generator for Fibonacci Numbers.

```py
# A simple generator for Fibonacci Numbers
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# Create a generator object
x = fib(5)
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())
  
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5): 
    print(i)
```
Output :
```
0
1
1
2
3

Using for in loop
0
1
1
2
3
```

## simple Python generator example
```py
def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3
```

Since the `greeting()` function contains the yield statements, it’s a generator function. The `yield` statement is like a `return` statement in a function. However, there’s a big difference.

When Python encounters the `yield` statement, it returns the value specified in the `yield`. In addition, it pauses the execution of the function.

If you `call` the same function again, Python will resume from where the previous `yield` statement was encountered.

When you call a generator function, it returns a generator object. For example:
```py
messenger = greeting()
```
The messenger is a generator object, which is also an iterator.

To actually execute the body of the `greeting()` function, you need to use the `next()` built-in function:
```py
result = next(messenger)
print(result)
```

When you the greeting() function executes, it shows the first message and returns 1:
```
Hi!
1
```
## Generator Class
The following example defines an iterator that returns a square number of an integer.
```py
class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2

        self.current += 1

        if self.current > self.length:
            raise StopIteration

        return result
```

The following rewrites the Squares iterator as a generator function:
```py
def squares(length):
    for n in range(length):
        yield n ** 2
```        


## Generator Expressions

A generator expression is an expression that returns a generator object. Basically, a generator function is a function that contains a `yield` statement and returns a generator object. 

For example, the following defines a generator function:

```py
def squares(length):
    for n in range(length):
        yield n ** 2
```
The `squares` generator function returns a generator object that produces square numbers of integers from `0` to `length - 1`.

Because a generator object is an iterator, you can use a for loop to iterate over its elements:
```py
for square in squares(5):
    print(square)
```

Output:
```
0
1
4
9
16
```

A generator expression provides you with a more simple way to return a generator object.

The following example defines a generator expression that returns square numbers of integers from 0 to 4:
```py
squares = (n** 2 for n in range(5))
```

Since the `squares` is a generator object, you can iterate over its elements like this:
```py
for square in squares:
    print(square)
```

As you can see, instead of using a function to define a generator function, you can use a generator expression.

A generator expression is like a list comprehension in terms of syntax. For example, a generator expression also supports complex syntaxes including:

- if statements
- Multiple nested loops
- Nested comprehensions

However, a generator expression uses the parentheses `()` instead of square brackets `[]`.


## Generator expressions vs list comprehensions
The following shows how to use the list comprehension to generate square numbers from 0 to 4:
```py
square_list = [n** 2 for n in range(5)]
```

And this defines a square number generator:
```py
square_generator = (n** 2 for n in range(5))
```

Differences
- A generator expression uses square brackets `[]` while a list comprehension uses parentheses `()`
- A list comprehension returns a list while a generator expression returns a generator object. It means that a list comprehension returns a complete list of elements upfront. However, a generator expression returns a list of elements, one at a time, based on request.
- A list comprehension is eager while a generator expression is lazy.In other words, a list comprehension creates all elements right away and loads all of them into the memory.
- A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again. However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausted when you complete iterating over it.


### Applications :
Suppose we to create a stream of Fibonacci numbers, adopting the generator approach makes it trivial; we just have to call next(x) to get the next Fibonacci number without bothering about where or when the stream of numbers ends.

A more practical type of stream processing is handling large data files such as log files. Generators provide a space efficient method for such data processing as only parts of the file are handled at one given point in time. We can also use Iterators for these purposes, but Generator provides a quick way (We don’t need to write `__next__` and `__iter__` methods here).


