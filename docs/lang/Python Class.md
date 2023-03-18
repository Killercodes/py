Python Class
====

## PUBLIC_CLASS_ATTRIBUTE
Class attributes are the variables defined directly in the class that are 
shared by all objects of the class. Class attributes can be accessed using 
the class name as well as using the objects. All members in a Python class 
are public by default. Any member can be accessed from outside the class environment.
```py
class PythonClass:
    schoolName = 'XYZ School' #class attribute
```

## PROTECTED CLASS ATTRIBUTE:
Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it.
this doesn't prevent instance variables from accessing or modifying the instance. See @property decorator below.
> Protected members of a class are accessible from within the class and are also available to its sub-classes
```py
class PythonClass:
    _proClassAttribute = "Protected members of a class"
```

## PRIVATE CLASS ATTRIBUTE:
The double underscore __ prefixed to a variable makes it private.
Prefixing the name of the variable/method with a single or double underscore to emulate the behavior of protected and private access specifiers.
```py
__pvtClassAttribute = "private member of a class"
```

##     INSTANCE ATTRIBUTE:
Instance attributes are attributes or properties attached to an instance of a class. 
Instance attributes are defined in the constructor. An instance attribute can be 
accessed using dot notation: [instance name].[attribute name]

```py
def __init__(self,myname,location="india"): #constructor with default value
    self.name = myname                      #instance attribute
    self.location = location                #instance attribute with defualt value
    self._pvtInsatnceAttribute = ''         #private instance attribute
```
## CLASS METHOD:
many class methods can be in a class using the def keyword. 
Each method must have the first parameter, generally named as self, 
which refers to the calling instance. Self is just a conventional name for the first 
argument of a method in the class. A method defined as mymethod(self, a, b) should be
called as x.mymethod(a, b) for the object x of the class.

```py
def setname(self,name): # instance function/class method
    self.name = name
```

## SELF:
The first parameter of the method need not be named self. You can give any name that 
refers to the instance of the calling method. The following displayInfo() method names 
the first parameter as obj instead of self and that works perfectly fine.
The method can access instance attributes using the self parameter.
```py
  def displayInfo(self): # class method
      print('Student Name: ', self.name,', Location: ', self.location)
```

##  PROPERTY:
The `property()` method in Python provides an interface to instance attributes. 
It encapsulates instance attributes and provides a property, same as Java and C#.
The `property()` method takes the get, set and delete methods as arguments and returns an object of the property class
```py
  def setpropery(self,value):
      self.__pvtInsatnceAttribute = value

  def getproperty(self):
      return  self.__pvtInsatnceAttribute
```

`property(getproperty,setpropery)` returns the property object and assigns 
it to name. Thus, the name property hides the private instance 
attribute `_pvtInsatnceAttribute`. The name property is accessed directly, 
but internally it will invoke the `getproperty()` or `setpropery()`
```py
    myproperty = property(getproperty,setpropery)
```

## PRIVATE CLASS METHOD:
```
    def __display(self):  # private method
        print("This is private method.")
```                

## DECORATOR FUNCTION:
The mydecorator() function takes a function as an argument. It calls the argument function and 
also prints some additional things. Thus, it extends the functionality of the greet() function
without modifying it. However, it is not the actual decorator.
```py
    def mydecorator(self,fn):
        fn()
        print('How are you?')
 ```   

The mydecorator() is not a decorator in Python. The decorator in Python can be defined over any 
appropriate function using the @decorator_function_name syntax to extend the functionality of the underlying function.
The inner function inner_function() can access the outer function's argument, so it executes some code before or after 
to extend the functionality before calling the argument function. The mydecorator function returns an inner function.
```py
    def mydecorator(fn):
        def inner_function():        
            fn()
            print('How are you?')
        return inner_function
```

Now, we can use mydecorator as a decorator to apply over a function that does not take any argument, as shown below.
The mydecorator can be applied to any function that does not require any argument.
```py
    @mydecorator
    def greet():
        print('Hello! ', end='')
```

## Built-in Decorators
Python library contains many built-in decorators as a shortcut of defining properties, class method, static methods, etc.

The @property decorator is a built-in decorator in Python for the property() function. Use @property decorator on any 
method in the class to use the method as a property.
You can use the following three decorators to define a property:
    @property: Declares the method as a property.
    @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
    @<property-name>.deleter: Specifies the delete method as a property that deletes a property.

### PROPERTY DECORATOR:
`@property` decorator is used to make the `proClassAttribute()` method as property 
and `@proClassAttribute.setter` decorator to another overloads of the `proClassAttribute()` method as 
property setter method. Now, `_proClassAttribute` is protected.
  
```py
  @property
  def proClassAttribute(self):
      return self._proClassAttribute

  @proClassAttribute.setter  #property-name.setter decorator
  def proClassAttribute(self,newname):
      self._proClassAttribute = newname
```
## Property Deleter
Use the `@property-name.deleter` decorator to define the method that deletes a property.
The deleter would be invoked when you delete the property using keyword del

```py
@proClassAttribute.deleter   #property-name.deleter decorator
def proClassAttribute(self, value):
    print('Deleting..')
    del self.__name
 ``` 
### CLASS METHOD DECORATOR
the `@classmethod` decorator is used to declare a method in the class as a class method that can be called 
using `ClassName.MethodName()`. The class method can also be called using an object of the class.

The @classmethod is an alternative of the `classmethod()` function. It is recommended to use the @classmethod
decorator instead of the function because it is just a syntactic sugar.

`@classmethod` Characteristics
- Declares a class method.
- The first parameter must be cls, which can be used to access class attributes.
- The class method can only access the class attributes but not the instance attributes.
- The class method can be called using ClassName.MethodName() and also using object.
- It can return an object of the class.

Note that the first parameter of any class method must be cls that can be used to access the class's attributes. 
You can give any name to the first parameter instead of cls. you can use the class method, as `PythonClass.tostring()` or with `object.tostring()`
The class method can only access class attributes, but not the instance attributes. 
It will raise an error if trying to access the instance attribute in the class method.

```py
@classmethod
def tostring(cls):
    print('Student Class Attributes: name=',cls.name)
```
  
The class method can also be used as a factory method to get an object of the class, as shown below.
  std = Student.getobject()
```py
@classmethod
def getobject(cls):
    return cls('Steve', "25 Lane")
```
  
### STATIC METHOD DECORATOR  
The @staticmethod is a built-in decorator that defines a static method in the class in Python. A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

@staticmethod Characteristics
- Declares a static method in the class.
- It cannot have cls or self parameter.
- The static method cannot access the class attributes or the instance attributes.
- The static method can be called using ClassName.MethodName() and also using object.MethodName().
- It can return an object of the class.

The static method can be called using the ClassName.MethodName() or object.MethodName().
The static method cannot access the class attributes or instance attributes. It will raise an error if try to do so.
```py
@staticmethod
def statictostring():
    print('Student Class')
```
  
@classmethod vs @staticmethod
The following table lists the difference between the class method and the static method:

@classmethod	
- Declares a class method.	
- It can access class attributes, but not the instance attributes.	
- It can be called using the ClassName.MethodName() or object.MethodName().	
- It can be used to declare a factory method that returns objects of the class.	

@staticmethod
- Declares a static method.
- It cannot access either class attributes or instance attributes.
- It can be called using the ClassName.MethodName() or object.MethodName().
- It cannot return an object of the class.
 
  
---

## Cheat sheet
```py
class PythonClass:

    """
    PUBLIC_CLASS_ATTRIBUTE
    """
    schoolName = 'XYZ School' #class attribute

    define+="""
    PROTECTED CLASS ATTRIBUTE:
    Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it.
    this doesn't prevent instance variables from accessing or modifying the instance. See @property decorator below
    """
    _proClassAttribute = "Protected members of a class are accessible from within the class and are also available to its sub-classes"

    define+="""
    PRIVATE CLASS ATTRIBUTE:
    The double underscore __ prefixed to a variable makes it private. 
    """
    __pvtClassAttribute = "Prefixing the name of the variable/method with a single or double underscore to emulate the behavior of protected and private access specifiers."

    define+="""
    INSTANCE ATTRIBUTE:
    Instance attributes are attributes or properties attached to an instance of a class. 
    Instance attributes are defined in the constructor. An instance attribute can be 
    accessed using dot notation: [instance name].[attribute name]
    """

    """"""
    def __init__(self,myname,location="india"): #constructor with default value
        self.name = myname                      #instance attribute
        self.location = location                #instance attribute with defualt value
        self._pvtInsatnceAttribute = ''         #private instance attribute

        define+="""
        CALSS METHOD:
        many class methods can be in a class using the def keyword. 
        Each method must have the first parameter, generally named as self, 
        which refers to the calling instance. Self is just a conventional name for the first 
        argument of a method in the class. A method defined as mymethod(self, a, b) should be
        called as x.mymethod(a, b) for the object x of the class.
        """

    def setname(self,name): # instance function/class method
        self.name = name

    define+="""
    SELF:
    The first parameter of the method need not be named self. You can give any name that 
    refers to the instance of the calling method. The following displayInfo() method names 
    the first parameter as obj instead of self and that works perfectly fine.
    The method can access instance attributes using the self parameter.
    """
    def displayInfo(self): # class method
        print('Student Name: ', self.name,', Location: ', self.location)

    define+="""
    PROPERTY:
    The property() method in Python provides an interface to instance attributes. 
    It encapsulates instance attributes and provides a property, same as Java and C#.
    The property() method takes the get, set and delete methods as arguments and returns an object of the property class
    """
    def setpropery(self,value):
        self.__pvtInsatnceAttribute = value
    
    def getproperty(self):
        return  self.__pvtInsatnceAttribute
    
    define+="""
    property(getproperty,setpropery) returns the property object and assigns 
    it to name. Thus, the name property hides the private instance 
    attribute _pvtInsatnceAttribute. The name property is accessed directly, 
    but internally it will invoke the getproperty() or setpropery()
    """
    myproperty = property(getproperty,setpropery)


    define+="""
    PRIVATE CLASS METHOD:
    """
    def __display(self):  # private method
        print("This is private method.")
                
    define+="""
    DECORATOR FUNCTION:
    the mydecorator() function takes a function as an argument. It calls the argument function and 
    also prints some additional things. Thus, it extends the functionality of the greet() function
    without modifying it. However, it is not the actual decorator.
    """
    def mydecorator(self,fn):
        fn()
        print('How are you?')
    
    define+="""
    The mydecorator() is not a decorator in Python. The decorator in Python can be defined over any 
    appropriate function using the @decorator_function_name syntax to extend the functionality of the underlying function.
    The inner function inner_function() can access the outer function's argument, so it executes some code before or after 
    to extend the functionality before calling the argument function. The mydecorator function returns an inner function.
    """
    def mydecorator(fn):
        def inner_function():        
            fn()
            print('How are you?')
        return inner_function
    
    define+="""
    Now, we can use mydecorator as a decorator to apply over a function that does not take any argument, as shown below.
    The mydecorator can be applied to any function that does not require any argument.
    """
    @mydecorator
    def greet():
        print('Hello! ', end='')

    define+="""
    Built-in Decorators
    Python library contains many built-in decorators as a shortcut of defining properties, class method, static methods, etc.
    """

    """
    The @property decorator is a built-in decorator in Python for the property() function. Use @property decorator on any 
    method in the class to use the method as a property.
    You can use the following three decorators to define a property:
        @property: Declares the method as a property.
        @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
        @<property-name>.deleter: Specifies the delete method as a property that deletes a property.
    """
    define+="""
    PROPERTY DECORATOR:
    @property decorator is used to make the proClassAttribute() method as property 
    and @proClassAttribute.setter decorator to another overloads of the proClassAttribute() method as 
    property setter method. Now, _proClassAttribute is protected.
    """
    @property
    def proClassAttribute(self):
        return self._proClassAttribute
    
    @proClassAttribute.setter  #property-name.setter decorator
    def proClassAttribute(self,newname):
        self._proClassAttribute = newname
    
    """
    Property Deleter
    Use the @property-name.deleter decorator to define the method that deletes a property.
    The deleter would be invoked when you delete the property using keyword del
    """
    @proClassAttribute.deleter   #property-name.deleter decorator
    def proClassAttribute(self, value):
        print('Deleting..')
        del self.__name

    """
    the @classmethod decorator is used to declare a method in the class as a class method that can be called 
    using ClassName.MethodName(). The class method can also be called using an object of the class.

    The @classmethod is an alternative of the classmethod() function. It is recommended to use the @classmethod
    decorator instead of the function because it is just a syntactic sugar.

    @classmethod Characteristics
    - Declares a class method.
    - The first parameter must be cls, which can be used to access class attributes.
    - The class method can only access the class attributes but not the instance attributes.
    - The class method can be called using ClassName.MethodName() and also using object.
    - It can return an object of the class.

    Note that the first parameter of any class method must be cls that can be used to access the class's attributes. 
    You can give any name to the first parameter instead of cls. you can use the class method, as PythonClass.tostring() or with object.tostring()
    The class method can only access class attributes, but not the instance attributes. 
    It will raise an error if trying to access the instance attribute in the class method.
    """
    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)

    """
    The class method can also be used as a factory method to get an object of the class, as shown below.
    std = Student.getobject()
    """
    @classmethod
    def getobject(cls):
        return cls('Steve', "25 Lane")
    
    """
    The @staticmethod is a built-in decorator that defines a static method in the class in Python. A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

    @staticmethod Characteristics
    - Declares a static method in the class.
    - It cannot have cls or self parameter.
    - The static method cannot access the class attributes or the instance attributes.
    - The static method can be called using ClassName.MethodName() and also using object.MethodName().
    - It can return an object of the class.

    The static method can be called using the ClassName.MethodName() or object.MethodName().
    The static method cannot access the class attributes or instance attributes. It will raise an error if try to do so.
    """
    @staticmethod
    def statictostring():
        print('Student Class')
    

    """
    @classmethod vs @staticmethod
    The following table lists the difference between the class method and the static method:

    @classmethod	
    - Declares a class method.	
    - It can access class attributes, but not the instance attributes.	
    - It can be called using the ClassName.MethodName() or object.MethodName().	
    - It can be used to declare a factory method that returns objects of the class.	

    @staticmethod
    - Declares a static method.
    - It cannot access either class attributes or instance attributes.
    - It can be called using the ClassName.MethodName() or object.MethodName().
    - It cannot return an object of the class.
    """
"""======================================================================================================================================"""

"""
Python - Magic or Dunder Methods
"""

""""
__new__()
In Python the __new__() magic method is implicitly called before the __init__() method. 
The __new__() method returns a new object, which is then initialized by __init__().
"""

class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'

"""
The following tables list important magic methods in Python 3.

Initialization and Construction	Description
__new__(cls, other)	To get called in an object's instantiation.
__init__(self, other)	To get called by the __new__ method.
__del__(self)	Destructor method.

Unary operators and functions	Description
__pos__(self)	To get called for unary positive e.g. +someobject.
__neg__(self)	To get called for unary negative e.g. -someobject.
__abs__(self)	To get called by built-in abs() function.
__invert__(self)	To get called for inversion using the ~ operator.
__round__(self,n)	To get called by built-in round() function.
__floor__(self)	To get called by built-in math.floor() function.
__ceil__(self)	To get called by built-in math.ceil() function.
__trunc__(self)	To get called by built-in math.trunc() function.

Augmented Assignment	Description
__iadd__(self, other)	To get called on addition with assignment e.g. a +=b.
__isub__(self, other)	To get called on subtraction with assignment e.g. a -=b.
__imul__(self, other)	To get called on multiplication with assignment e.g. a *=b.
__ifloordiv__(self, other)	To get called on integer division with assignment e.g. a //=b.
__idiv__(self, other)	To get called on division with assignment e.g. a /=b.
__itruediv__(self, other)	To get called on true division with assignment
__imod__(self, other)	To get called on modulo with assignment e.g. a%=b.
__ipow__(self, other)	To get called on exponentswith assignment e.g. a **=b.
__ilshift__(self, other)	To get called on left bitwise shift with assignment e.g. a<<=b.
__irshift__(self, other)	To get called on right bitwise shift with assignment e.g. a >>=b.
__iand__(self, other)	To get called on bitwise AND with assignment e.g. a&=b.
__ior__(self, other)	To get called on bitwise OR with assignment e.g. a|=b.
__ixor__(self, other)	To get called on bitwise XOR with assignment e.g. a ^=b.

Type Conversion Magic Methods	Description
__int__(self)	To get called by built-int int() method to convert a type to an int.
__float__(self)	To get called by built-int float() method to convert a type to float.
__complex__(self)	To get called by built-int complex() method to convert a type to complex.
__oct__(self)	To get called by built-int oct() method to convert a type to octal.
__hex__(self)	To get called by built-int hex() method to convert a type to hexadecimal.
__index__(self)	To get called on type conversion to an int when the object is used in a slice expression.
__trunc__(self)	To get called from math.trunc() method.

String Magic Methods	Description
__str__(self)	To get called by built-int str() method to return a string representation of a type.
__repr__(self)	To get called by built-int repr() method to return a machine readable representation of a type.
__unicode__(self)	To get called by built-int unicode() method to return an unicode string of a type.
__format__(self, formatstr)	To get called by built-int string.format() method to return a new style of string.
__hash__(self)	To get called by built-int hash() method to return an integer.
__nonzero__(self)	To get called by built-int bool() method to return True or False.
__dir__(self)	To get called by built-int dir() method to return a list of attributes of a class.
__sizeof__(self)	To get called by built-int sys.getsizeof() method to return the size of an object.

Attribute Magic Methods	Description
__getattr__(self, name)	Is called when the accessing attribute of a class that does not exist.
__setattr__(self, name, value)	Is called when assigning a value to the attribute of a class.
__delattr__(self, name)	Is called when deleting an attribute of a class.

Operator Magic Methods	Description
__add__(self, other)	To get called on add operation using + operator
__sub__(self, other)	To get called on subtraction operation using - operator.
__mul__(self, other)	To get called on multiplication operation using * operator.
__floordiv__(self, other)	To get called on floor division operation using // operator.
__truediv__(self, other)	To get called on division operation using / operator.
__mod__(self, other)	To get called on modulo operation using % operator.
__pow__(self, other[, modulo])	To get called on calculating the power using ** operator.
__lt__(self, other)	To get called on comparison using < operator.
__le__(self, other)	To get called on comparison using <= operator.
__eq__(self, other)	To get called on comparison using == operator.
__ne__(self, other)	To get called on comparison using != operator.
__ge__(self, other)	To get called on comparison using >= operator.




```py
class PythonClass:

    define="""
    PUBLIC_CLASS_ATTRIBUTE
    Class attributes are the variables defined directly in the class that are 
    shared by all objects of the class. Class attributes can be accessed using 
    the class name as well as using the objects. All members in a Python class 
    are public by default. Any member can be accessed from outside the class environment.
    """
    schoolName = 'XYZ School' #class attribute

    define+="""
    PROTECTED CLASS ATTRIBUTE:
    Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it.
    this doesn't prevent instance variables from accessing or modifying the instance. See @property decorator below
    """
    _proClassAttribute = "Protected members of a class are accessible from within the class and are also available to its sub-classes"

    define+="""
    PRIVATE CLASS ATTRIBUTE:
    The double underscore __ prefixed to a variable makes it private. 
    """
    __pvtClassAttribute = "Prefixing the name of the variable/method with a single or double underscore to emulate the behavior of protected and private access specifiers."

    define+="""
    INSTANCE ATTRIBUTE:
    Instance attributes are attributes or properties attached to an instance of a class. 
    Instance attributes are defined in the constructor. An instance attribute can be 
    accessed using dot notation: [instance name].[attribute name]
    """

    """"""
    def __init__(self,myname,location="india"): #constructor with default value
        self.name = myname                      #instance attribute
        self.location = location                #instance attribute with defualt value
        self._pvtInsatnceAttribute = ''         #private instance attribute

        define+="""
        CALSS METHOD:
        many class methods can be in a class using the def keyword. 
        Each method must have the first parameter, generally named as self, 
        which refers to the calling instance. Self is just a conventional name for the first 
        argument of a method in the class. A method defined as mymethod(self, a, b) should be
        called as x.mymethod(a, b) for the object x of the class.
        """

    def setname(self,name): # instance function/class method
        self.name = name

    define+="""
    SELF:
    The first parameter of the method need not be named self. You can give any name that 
    refers to the instance of the calling method. The following displayInfo() method names 
    the first parameter as obj instead of self and that works perfectly fine.
    The method can access instance attributes using the self parameter.
    """
    def displayInfo(self): # class method
        print('Student Name: ', self.name,', Location: ', self.location)

    define+="""
    PROPERTY:
    The property() method in Python provides an interface to instance attributes. 
    It encapsulates instance attributes and provides a property, same as Java and C#.
    The property() method takes the get, set and delete methods as arguments and returns an object of the property class
    """
    def setpropery(self,value):
        self.__pvtInsatnceAttribute = value
    
    def getproperty(self):
        return  self.__pvtInsatnceAttribute
    
    define+="""
    property(getproperty,setpropery) returns the property object and assigns 
    it to name. Thus, the name property hides the private instance 
    attribute _pvtInsatnceAttribute. The name property is accessed directly, 
    but internally it will invoke the getproperty() or setpropery()
    """
    myproperty = property(getproperty,setpropery)


    define+="""
    PRIVATE CLASS METHOD:
    """
    def __display(self):  # private method
        print("This is private method.")
                
    define+="""
    DECORATOR FUNCTION:
    the mydecorator() function takes a function as an argument. It calls the argument function and 
    also prints some additional things. Thus, it extends the functionality of the greet() function
    without modifying it. However, it is not the actual decorator.
    """
    def mydecorator(self,fn):
        fn()
        print('How are you?')
    
    define+="""
    The mydecorator() is not a decorator in Python. The decorator in Python can be defined over any 
    appropriate function using the @decorator_function_name syntax to extend the functionality of the underlying function.
    The inner function inner_function() can access the outer function's argument, so it executes some code before or after 
    to extend the functionality before calling the argument function. The mydecorator function returns an inner function.
    """
    def mydecorator(fn):
        def inner_function():        
            fn()
            print('How are you?')
        return inner_function
    
    define+="""
    Now, we can use mydecorator as a decorator to apply over a function that does not take any argument, as shown below.
    The mydecorator can be applied to any function that does not require any argument.
    """
    @mydecorator
    def greet():
        print('Hello! ', end='')

    define+="""
    Built-in Decorators
    Python library contains many built-in decorators as a shortcut of defining properties, class method, static methods, etc.
    """

    """
    The @property decorator is a built-in decorator in Python for the property() function. Use @property decorator on any 
    method in the class to use the method as a property.
    You can use the following three decorators to define a property:
        @property: Declares the method as a property.
        @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
        @<property-name>.deleter: Specifies the delete method as a property that deletes a property.
    """
    define+="""
    PROPERTY DECORATOR:
    @property decorator is used to make the proClassAttribute() method as property 
    and @proClassAttribute.setter decorator to another overloads of the proClassAttribute() method as 
    property setter method. Now, _proClassAttribute is protected.
    """
    @property
    def proClassAttribute(self):
        return self._proClassAttribute
    
    @proClassAttribute.setter  #property-name.setter decorator
    def proClassAttribute(self,newname):
        self._proClassAttribute = newname
    
    """
    Property Deleter
    Use the @property-name.deleter decorator to define the method that deletes a property.
    The deleter would be invoked when you delete the property using keyword del
    """
    @proClassAttribute.deleter   #property-name.deleter decorator
    def proClassAttribute(self, value):
        print('Deleting..')
        del self.__name

    """
    the @classmethod decorator is used to declare a method in the class as a class method that can be called 
    using ClassName.MethodName(). The class method can also be called using an object of the class.

    The @classmethod is an alternative of the classmethod() function. It is recommended to use the @classmethod
    decorator instead of the function because it is just a syntactic sugar.

    @classmethod Characteristics
    - Declares a class method.
    - The first parameter must be cls, which can be used to access class attributes.
    - The class method can only access the class attributes but not the instance attributes.
    - The class method can be called using ClassName.MethodName() and also using object.
    - It can return an object of the class.

    Note that the first parameter of any class method must be cls that can be used to access the class's attributes. 
    You can give any name to the first parameter instead of cls. you can use the class method, as PythonClass.tostring() or with object.tostring()
    The class method can only access class attributes, but not the instance attributes. 
    It will raise an error if trying to access the instance attribute in the class method.
    """
    @classmethod
    def tostring(cls):
        print('Student Class Attributes: name=',cls.name)

    """
    The class method can also be used as a factory method to get an object of the class, as shown below.
    std = Student.getobject()
    """
    @classmethod
    def getobject(cls):
        return cls('Steve', "25 Lane")
    
    """
    The @staticmethod is a built-in decorator that defines a static method in the class in Python. A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.

    @staticmethod Characteristics
    - Declares a static method in the class.
    - It cannot have cls or self parameter.
    - The static method cannot access the class attributes or the instance attributes.
    - The static method can be called using ClassName.MethodName() and also using object.MethodName().
    - It can return an object of the class.

    The static method can be called using the ClassName.MethodName() or object.MethodName().
    The static method cannot access the class attributes or instance attributes. It will raise an error if try to do so.
    """
    @staticmethod
    def statictostring():
        print('Student Class')
    

    """
    @classmethod vs @staticmethod
    The following table lists the difference between the class method and the static method:

    @classmethod	
    - Declares a class method.	
    - It can access class attributes, but not the instance attributes.	
    - It can be called using the ClassName.MethodName() or object.MethodName().	
    - It can be used to declare a factory method that returns objects of the class.	

    @staticmethod
    - Declares a static method.
    - It cannot access either class attributes or instance attributes.
    - It can be called using the ClassName.MethodName() or object.MethodName().
    - It cannot return an object of the class.
    """
"""======================================================================================================================================"""

"""
Python - Magic or Dunder Methods
"""

""""
__new__()
In Python the __new__() magic method is implicitly called before the __init__() method. 
The __new__() method returns a new object, which is then initialized by __init__().
"""

class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'

"""
The following tables list important magic methods in Python 3.

Initialization and Construction	Description
__new__(cls, other)	To get called in an object's instantiation.
__init__(self, other)	To get called by the __new__ method.
__del__(self)	Destructor method.

Unary operators and functions	Description
__pos__(self)	To get called for unary positive e.g. +someobject.
__neg__(self)	To get called for unary negative e.g. -someobject.
__abs__(self)	To get called by built-in abs() function.
__invert__(self)	To get called for inversion using the ~ operator.
__round__(self,n)	To get called by built-in round() function.
__floor__(self)	To get called by built-in math.floor() function.
__ceil__(self)	To get called by built-in math.ceil() function.
__trunc__(self)	To get called by built-in math.trunc() function.

Augmented Assignment	Description
__iadd__(self, other)	To get called on addition with assignment e.g. a +=b.
__isub__(self, other)	To get called on subtraction with assignment e.g. a -=b.
__imul__(self, other)	To get called on multiplication with assignment e.g. a *=b.
__ifloordiv__(self, other)	To get called on integer division with assignment e.g. a //=b.
__idiv__(self, other)	To get called on division with assignment e.g. a /=b.
__itruediv__(self, other)	To get called on true division with assignment
__imod__(self, other)	To get called on modulo with assignment e.g. a%=b.
__ipow__(self, other)	To get called on exponentswith assignment e.g. a **=b.
__ilshift__(self, other)	To get called on left bitwise shift with assignment e.g. a<<=b.
__irshift__(self, other)	To get called on right bitwise shift with assignment e.g. a >>=b.
__iand__(self, other)	To get called on bitwise AND with assignment e.g. a&=b.
__ior__(self, other)	To get called on bitwise OR with assignment e.g. a|=b.
__ixor__(self, other)	To get called on bitwise XOR with assignment e.g. a ^=b.

Type Conversion Magic Methods	Description
__int__(self)	To get called by built-int int() method to convert a type to an int.
__float__(self)	To get called by built-int float() method to convert a type to float.
__complex__(self)	To get called by built-int complex() method to convert a type to complex.
__oct__(self)	To get called by built-int oct() method to convert a type to octal.
__hex__(self)	To get called by built-int hex() method to convert a type to hexadecimal.
__index__(self)	To get called on type conversion to an int when the object is used in a slice expression.
__trunc__(self)	To get called from math.trunc() method.

String Magic Methods	Description
__str__(self)	To get called by built-int str() method to return a string representation of a type.
__repr__(self)	To get called by built-int repr() method to return a machine readable representation of a type.
__unicode__(self)	To get called by built-int unicode() method to return an unicode string of a type.
__format__(self, formatstr)	To get called by built-int string.format() method to return a new style of string.
__hash__(self)	To get called by built-int hash() method to return an integer.
__nonzero__(self)	To get called by built-int bool() method to return True or False.
__dir__(self)	To get called by built-int dir() method to return a list of attributes of a class.
__sizeof__(self)	To get called by built-int sys.getsizeof() method to return the size of an object.

Attribute Magic Methods	Description
__getattr__(self, name)	Is called when the accessing attribute of a class that does not exist.
__setattr__(self, name, value)	Is called when assigning a value to the attribute of a class.
__delattr__(self, name)	Is called when deleting an attribute of a class.

Operator Magic Methods	Description
__add__(self, other)	To get called on add operation using + operator
__sub__(self, other)	To get called on subtraction operation using - operator.
__mul__(self, other)	To get called on multiplication operation using * operator.
__floordiv__(self, other)	To get called on floor division operation using // operator.
__truediv__(self, other)	To get called on division operation using / operator.
__mod__(self, other)	To get called on modulo operation using % operator.
__pow__(self, other[, modulo])	To get called on calculating the power using ** operator.
__lt__(self, other)	To get called on comparison using < operator.
__le__(self, other)	To get called on comparison using <= operator.
__eq__(self, other)	To get called on comparison using == operator.
__ne__(self, other)	To get called on comparison using != operator.
__ge__(self, other)	To get called on comparison using >= operator.
"""
```
