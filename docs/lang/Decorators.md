# Python Decorators

In general, a decorator is:

- A function that takes another function (original function) as an argument and returns another function (or closure)
- The closure typically accepts any combination of positional and keyword-only arguments.
- The closure function calls the original function using the arguments passed to the closure and returns the result of the function.

By definition, a decorator is a function that takes a function as an argument and it returns another function:

```py
def netSalary(price,tax):
    return price *(1+tax)

# decorator function
def currency(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)

    return wrapper

```



The `currency` function returns the `wrapper` function. The `wrapper` function has the `*args` and `**kwargs` parameters. These parameters allow you to call any fn function with any combination of positional and keyword-only arguments.

In this example, the wrapper function essentially executes the fn function directly and doesn’t change any behavior of the fn function.

In the wrapper function, you can call the fn function, get its result, and format the result as a currency string:
```py
def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper
```

The `currency` function is now a decorator.

It accepts any function that returns a number and format that number as a currency string.

To use the `currency` decorator, you need to pass the `netSalary` function to it to get a new function and execute the new function as if it were the original function. For example:
```py
netSalary = currency(netSalary)
print(netSalary(100, 0.05))
```
Output:
```
$105.0
```

## The @ symbol
In the previous example, the currency is a decorator. And you can decorate the netSalary function using the following syntax:
```py
netSalary = currency(netSalary)
```
Generally, if decorate is a decorator function and you want to decorate another function fn, you can use this syntax:
```
fn = decorate(fn)
```
To make it more convenient, Python provides a shorter way like this:
```py
@decorate
def fn():
    pass
```
For example, instead of using the following syntax:
```
netSalary = currency(netSalary)
```
… you can decorate the `netSalary` function using the `@currency` as follows:
```py
@currency
def netSalary(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)
```
Put it all together.
```py
def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def netSalary(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


print(netSalary(100, 0.05))
```

## Introspecting decorated functions

When you decorate a function:
```py
@decorate
def fn(*args,**kwargs):
    pass
```
It’s equivalent:
```
fn = decorate(fn)
```
The `decorate` function returns a new function, which is the wrapper function.

If you use the built-in `help` function to show the documentation of the new function, you won’t see the documentation of the original function. For example:
```py
help(netSalary)
```
Output:
```
wrapper(*args, **kwargs)

None
```

Also, if you check the name of the new function, Python will return the name of the inner function returned by the decorator:
```py
print(netSalary.__name__)
```

Output:
```
wrapper
```
So when you decorate a function, you’ll lose the original function signature and documentation.

To fix this, you can use the `wraps` function from the functools standard module. In fact, the `wraps` function is also a decorator.

The following shows how to use the `wraps` decorator:
```py
from functools import wraps


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def netSalary(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


help(netSalary)
print(netSalary.__name__)
```

Output:
```
netSalary(price, tax)
    calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price

netSalary    
```

## Summary
- A decorator is a function that changes the behavior of another function without explicitly modifying it.
- Use the `@` symbol to decorate a function.
- Use the `wraps` function from the functools built-in module to retain the documentation and name of the original function.

## Decorator with Arguments

The follwoing is an exmple of a decorator that prints the messages 5 times:

```py
from functools import wraps

def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result

    return wrapper


@repeat
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')

```

In the example above, it has a hardcoded value of 5 to print 5 times what if you want to make it parameterized so that it print _n_ number of times.

The modified code should look as the following:
```py

from functools import wraps


def repeat(times):
    ''' call a function a number of times '''
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate


@repeat(10)
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')


```
