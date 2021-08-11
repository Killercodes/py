# Loops
In general, statements are executed sequentially − The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times.

Programming languages provide various control structures that allow more complicated execution paths.

A loop statement allows us to execute a statement or group of statements multiple times. The following diagram illustrates a loop statement −

Loop Architecture
Python programming language provides the following types of loops to handle looping requirements.

Loop Type | Description
----|----
while loop|Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.
for loop|Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
nested loops|You can use one or more loop inside any another while, or for loop.

## while Loop Statements
A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.

**Syntax**
The syntax of a while loop in Python programming language is −
```
while expression:
   statement(s)
```
Here, statement(s) may be a single statement or a block of statements with uniform indent. The condition may be any expression, and true is any non-zero value. The loop iterates while the condition is true.

When the condition becomes false, program control passes to the line immediately following the loop.

In Python, all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements.

Here, a key point of the while loop is that the loop might not ever run. When the condition is tested and the result is false, the loop body will be skipped and the first statement after the while loop will be executed.

**Example**
```python
#!/usr/bin/python3

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")
```
**Output**

When the above code is executed, it produces the following result −
```
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
Good bye!
```
The block here, consisting of the print and increment statements, is executed repeatedly until count is no longer less than 9. With each iteration, the current value of the index count is displayed and then increased by 1.

### The Infinite Loop
A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious when using while loops because of the possibility that this condition never resolves to a FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.

An infinite loop might be useful in client/server programming where the server needs to run continuously so that client programs can communicate with it as and when required.

Example
```python
#!/usr/bin/python3

var = 1
while var == 1 :  # This constructs an infinite loop
   num = int(input("Enter a number  :"))
   print ("You entered: ", num)

print ("Good bye!")
```
**Output**
When the above code is executed, it produces the following result −
```
Enter a number  :20
You entered:  20
Enter a number  :29
You entered:  29
Enter a number  :3
You entered:  3
Enter a number  :11
You entered:  11
Enter a number  :22
You entered:  22
Enter a number  :Traceback (most recent call last):
   File "examples\test.py", line 5, in 
      num = int(input("Enter a number  :"))
KeyboardInterrupt
```
The above example goes in an infinite loop and you need to use CTRL+C to exit the program.

### Using else Statement with Loops
Python supports having an else statement associated with a loop statement.

If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

The following example illustrates the combination of an else statement with a while statement that prints a number as long as it is less than 5, otherwise the else statement gets executed.

**Example**
```python
#!/usr/bin/python3

count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
```   
**Output**
When the above code is executed, it produces the following result −
```
0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
```
### Single Statement Suites
Similar to the if statement syntax, if your while clause consists only of a single statement, it may be placed on the same line as the while header.

**Example**
Here is the syntax and example of a one-line while clause −
```python
#!/usr/bin/python3

flag = 1
while (flag): print ('Given flag is really true!')
print ("Good bye!")
```
The above example goes into an infinite loop and you need to press CTRL+C keys to exit.

## for loop Statements
The for statement in Python has the ability to iterate over the items of any sequence, such as a list or a string.

**Syntax**
```
for iterating_var in sequence:
   statements(s)
```
If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable `iterating_var`. Next, the `statements` block is executed. Each item in the list is assigned to iterating_var, and the `statement(s)` block is executed until the entire sequence is exhausted.

### The range() function
The built-in function range() is the right function to iterate over a sequence of numbers. It generates an iterator of arithmetic progressions.

Example
```python
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```
**Example**

**range()** generates an iterator to progress integers starting with 0 upto n-1. To obtain a list object of the sequence, it is typecasted to list(). Now this list can be iterated using the for statement.
```python
>>> for var in list(range(5)):
   print (var)
```
**Output**
This will produce the following output.
```
0
1
2
3
4
```
**Example**
```python
#!/usr/bin/python3

for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")
```
**Output**
When the above code is executed, it produces the following result −
```
Current Letter : P
Current Letter : y
Current Letter : t
Current Letter : h
Current Letter : o
Current Letter : n

Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye!
```
### Iterating by Sequence Index
An alternative way of iterating through each item is by index offset into the sequence itself. Following is a simple example −

Example
```python
#!/usr/bin/python3

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

print ("Good bye!")
```
**Output**

When the above code is executed, it produces the following result −
```
Current fruit : banana
Current fruit : apple
Current fruit : mango
Good bye!
```
Here, we took the assistance of the len() built-in function, which provides the total number of elements in the tuple as well as the range() built-in function to give us the actual sequence to iterate over.

### Using else Statement with Loops
Python supports having an else statement associated with a loop statement.

If the else statement is used with a for loop, the else block is executed only if for loops terminates normally (and not by encountering break statement).

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

**Example**
The following example illustrates the combination of an else statement with a for statement that searches for even number in given list.
``` python
#!/usr/bin/python3

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')
```
**Output**
When the above code is executed, it produces the following result −
```
the list does not contain even number
```
## Nested Loops
Python programming language allows the usage of one loop inside another loop. The following section shows a few examples to illustrate the concept.

Syntax
```for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```
The syntax for a nested while loop statement in Python programming language is as follows −
```
while expression:
   while expression:
      statement(s)
   statement(s)
```
A final note on loop nesting is that you can put any type of loop inside any other type of loop. For example a for loop can be inside a while loop or vice versa.

**Example**
The following program uses a nested-for loop to display multiplication tables from 1-10.
```python
#!/usr/bin/python3
import sys
for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print (k, end=' ')
   print()
```   
The print() function inner loop has end=' ' which appends a space instead of default newline. Hence, the numbers will appear in one row.

Last print() will be executed at the end of inner for loop.

**Output**
When the above code is executed, it produces the following result −
```
1 2 3 4 5 6 7 8 9 10 
2 4 6 8 10 12 14 16 18 20 
3 6 9 12 15 18 21 24 27 30 
4 8 12 16 20 24 28 32 36 40 
5 10 15 20 25 30 35 40 45 50 
6 12 18 24 30 36 42 48 54 60 
7 14 21 28 35 42 49 56 63 70 
8 16 24 32 40 48 56 64 72 80 
9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 
```

## Loop Control Statements
The Loop control statements change the execution from its normal sequence. When the execution leaves a scope, all automatic objects that were created in that scope are destroyed.

Python supports the following control statements.

Control Statement | Description
----|----
break statement|Terminates the loop statement and transfers execution to the statement immediately following the loop.
continue statement|Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
pass statement|The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

Let us go through the loop control statements briefly.

## Iterator and Generator
Iterator is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. In Python, an iterator object implements two methods, iter() and next().

String, List or Tuple objects can be used to create an Iterator.
```
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
```
Iterator object can be traversed using regular for statement
``` python
!usr/bin/python3
for x in it:
   print (x, end=" ")
or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
```      
A **generator** is a function that produces or yields a sequence of values using yield method.

When a generator function is called, it returns a generator object without even beginning execution of the function. When the next() method is called for the first time, the function starts executing until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e. remembers the last execution and the second next() call continues from previous value.

**Example**
The following example defines a generator, which generates an iterator for all the Fibonacci numbers.
```python
!usr/bin/python3
import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
```  
