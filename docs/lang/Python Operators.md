# Python Operators

## Basic Operators
Operators are the constructs, which can manipulate the value of operands. Consider the expression `4 + 5 = 9`. Here, `4` and `5` are called the operands and `+` is called the operator.

Types of Operator
Python language supports the following types of operators −

- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators
Let us have a look at all the operators one by one.

## Python Arithmetic Operators
Assume variable a holds the value 10 and variable b holds the value 21, then −

``` python
#!/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c )

c = a * b
print ("Line 3 - Value of c is ", c)

c = a / b
print ("Line 4 - Value of c is ", c )

c = a % b
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b 
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b 
print ("Line 7 - Value of c is ", c)
```

Operator|Define|	Description|	Example
----|----|----|----
`+`| Addition|	Adds values on either side of the operator.|	`a + b = 31`
`-`| Subtraction|	Subtracts right hand operand from left hand operand.|	`a – b = -11`
`*`| Multiplication|	Multiplies values on either side of the operator|	`a * b = 210`
`/`| Division|	Divides left hand operand by right hand operand|	`b / a = 2.1`
`%`| Modulus|	Divides left hand operand by right hand operand and returns remainder|	`b % a = 1`
`**`| Exponent|	Performs exponential (power) calculation on operators|	`a**b =10 to the power 20`
`//`|	Floor Division| The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity):|	`9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0`

## Python Comparison Operators
These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Assume variable a holds the value 10 and variable b holds the value 20, then −

``` python
#!/usr/bin/python3

a = 21
b = 10

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")
```

Operator|	Description|	Example
----|----|----
`==`| If the values of two operands are equal, then the condition becomes true.	|(a == b) is not true.
`!=`|	If values of two operands are not equal, then condition becomes true.|	(a!= b) is true.
`>` |	If the value of left operand is greater than the value of right operand, then condition becomes true.|	(a > b) is not true.
`<` |	If the value of left operand is less than the value of right operand, then condition becomes true.|	(a < b) is true.`
`>=`|	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.|	(a >= b) is not true.
`<=`|	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.|	(a <= b) is true.

the output will be
```
Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not less than b
Line 4 - a is greater than b
Line 5 - a is either less than or equal to  b
Line 6 - b is either greater than  or equal to b
```
## Python Assignment Operators
Assume variable a holds the value 10 and variable b holds the value 20, then −

``` python
#!/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c )

c *= a
print ("Line 3 - Value of c is ", c )

c /= a 
print ("Line 4 - Value of c is ", c )

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)
```

Operator|Define	|Description|	Example
----|----|----|----
`=`|Assign	|Assigns values from right side operands to left side operand|	`c = a + b assigns value of a + b into c`
`+=` |Add AND|	It adds right operand to the left operand and assign the result to left operand|	`c += a is equivalent to c = c + a`
`-=`| Subtract AND|	It subtracts right operand from the left operand and assign the result to left operand|	`c -= a is equivalent to c = c - a`
`*=`| Multiply AND|	It multiplies right operand with the left operand and assign the result to left operand|	`c *= a is equivalent to c = c * a`
`/=`| Divide AND|	It divides left operand with the right operand and assign the result to left operand|	`c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a`
`%=`| Modulus AND|	It takes modulus using two operands and assign the result to left |operand	`c %= a is equivalent to c = c % a`
`**=`| Exponent AND|	Performs exponential (power) calculation on operators and assign value to the left operand|	`c **= a is equivalent to c = c ** a`
`//=`| Floor Division|	It performs floor division on operators and assign value to the left operand|	`c //= a is equivalent to c = c // a`

The output
```
Line 1 - Value of c is  31
Line 2 - Value of c is  52
Line 3 - Value of c is  1092
Line 4 - Value of c is  52.0
Line 5 - Value of c is  2
Line 6 - Value of c is  2097152
Line 7 - Value of c is  99864
```
## Python Bitwise Operators
Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows −
```
a = 0011 1100
b = 0000 1101
-----------------

a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a = 1100 0011
```

Python's built-in function `bin()` can be used to obtain binary representation of an integer number.

The following Bitwise operators are supported by Python language −

```py
#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))

c = a | b;        # 61 = 0011 1101 
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))
```

Operator|	Define | Description|	Example
----|----|----|----
`& `|Binary AND|	Operator copies a bit, to the result, if it exists in both operands|	`(a & b)` (means 0000 1100)
`|`| Binary OR|	It copies a bit, if it exists in either operand.|	`(a | b) = 61` (means 0011 1101)
`^`| Binary XOR|	It copies the bit, if it is set in one operand but not both.|	`(a ^ b) = 49` (means 0011 0001)
`~`| Binary Ones Complement|	It is unary and has the effect of 'flipping' bits.|	`(~a ) = -61` (means 1100 0011 in 2's complement form due to a signed binary number.
`<<`| Binary Left Shift|	The left operand's value is moved left by the number of bits specified by the right operand.|	`a << = 240` (means 1111 0000)
`>>`| Binary Right Shift|	The left operand's value is moved right by the number of bits specified by the right operand.|	`a >> = 15` (means 0000 1111)

```
a = 60 : 0b111100 b = 13 : 0b1101
result of AND is  12 : 0b1100
result of OR is  61 : 0b111101
result of EXOR is  49 : 0b110001
result of COMPLEMENT is  -61 : -0b111101
result of LEFT SHIFT is  240 : 0b11110000
result of RIGHT SHIFT is  15 : 0b111
```
## Python Logical Operators
The following logical operators are supported by Python language. Assume variable a holds True and variable b holds False then −

Operator|	Define|Description|	Example
----|----|----|----
`and`| Logical AND|	If both the operands are true then condition becomes true.	|`(a and b)` is False.
`or`| Logical OR|	If any of the two operands are non-zero then condition becomes true.|	`(a or b)` is True.
`not`| Logical NOT|	Used to reverse the logical state of its operand.|	`Not(a and b)` is True.


## Python Membership Operators
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below −

```python
#!/usr/bin/python3

a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

c=b/a
if ( c in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")
```

Operator|	Define\Description|	Example
----|----|----|----
`in`|	Evaluates to true |if it finds a variable in the specified sequence and false otherwise.|	x in y, here in results in a 1 if x is a member of sequence y.
`not in`|	Evaluates to true |if it does not finds a variable in the specified sequence and false otherwise.|	x not in y, here not in results in a 1 if x is not a member of sequence y.

The Output
```
Line 1 - a is not available in the given list
Line 2 - b is not available in the given list
Line 3 - a is available in the given list
```

## Python Identity Operators
Identity operators compare the memory locations of two objects. There are two Identity operators as explained below −

```python
#!/usr/bin/python3

a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is not b ):
   print ("Line 5 - a and b do not have same identity")
else:
   print ("Line 5 - a and b have same identity")
```

Operator|	Define| Description|	Example
----|----|----|----
`is`|	Evaluates to true| if the variables on either side of the operator point to the same object and false otherwise.|	x is y, here is results in 1 if id(x) equals id(y).
`is not`|	Evaluates to false| if the variables on either side of the operator point to the same object and true otherwise.|	x is not y, here is not results in 1 if id(x) is not equal to id(y).

```
Line 1 a= 20 : 1594701888 b= 20 : 1594701888
Line 2 - a and b have same identity
Line 3 - a and b have same identity
Line 4 a= 20 : 1594701888 b= 30 : 1594702048
Line 5 - a and b do not have same identity
```

## Python Operators Precedence
The following table lists all operators from highest precedence to the lowest.

Show Example

Operator | Description
----|----
`**`|Exponentiation (raise to the power)
`~ + -`|Ccomplement, unary plus and minus (method names for the last two are +@ and -@)
`* / % //`|Multiply, divide, modulo and floor division
`+ -`|Addition and subtraction
`>> <<`|Right and left bitwise shift
`&`|Bitwise 'AND'	
`^\`| |Bitwise exclusive `OR' and regular `OR'
`<= < > >=`|Comparison operators
`<> == !=`|Equality operators
`= %= /= //= -= += *= **=`|Assignment operators
`is is not`|Identity operators
`in not in`|Membership operators
`not or and`|Logical operators

