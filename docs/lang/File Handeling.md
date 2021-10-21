# Python File Handeling

Python treats file differently as text or binary and this is important. Each line of code includes a sequence of characters and they form text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with Reading and Writing files.

## Working of open() function

We use open () function in Python to open a file in read or write mode. As explained above, open ( ) will return a file object. To return a file object we use open() function along with two arguments, that accepts file name and the mode, whether to read or write. So, the syntax being: open(filename, mode). There are three kinds of mode, that Python provides and how files can be opened:

```
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing
```
One must keep in mind that the mode argument is not mandatory. If not passed, then Python will assume it to be “ r ” by default. Let’s look at this program and try to analyze how the read mode works:

```py
# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
```
The open command will open the file in the read mode and the for loop will print each line present in the file.



## Working of read() mode

There is more than one way to read a file in Python. If you need to extract a string that contains all characters in the file then we can use file.read(). The full code would work like this:

```py
# Python code to illustrate read() mode
file = open("file.text", "r") 
print (file.read())
```
Another way to read a file is to call a certain number of characters like in the following code the interpreter will read the first five characters of stored data and return it as a string:
```py
# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))
```

## Creating a file using write() mode

Let’s see how to create a file and how write mode works:
To manipulate the file, write the following in your Python environment:
```py
# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
```
The close() command terminates all the resources in use and frees the system of this particular program.

## Working of append() mode

Let’s see how the append mode works:
```py
# Python code to illustrate append() mode
file = open('geek.txt','a')
file.write("This will add this line")
file.close()
```
There are also various other commands in file handling that is used to handle various tasks like:

```rstrip()```: This function strips each line of a file off spaces from the right-hand side.
```lstrip()```: This function strips each line of a file off spaces from the left-hand side.

It is designed to provide much cleaner syntax and exceptions handling when you are working with code. That explains why it’s good practice to use them with a statement where applicable. This is helpful because using this method any files opened will be closed automatically after one is done, so auto-cleanup.
Example:
```py
# Python code to illustrate with()
with open("file.txt") as file:  
    data = file.read() 
# do something with data 
```

## Using write along with with() function

We can also use write function along with with() function:
```py
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f: 
    f.write("Hello World!!!") 
```
## split() using file handling

We can also split lines using file handling in Python. This splits the variable when space is encountered. You can also split using any characters as we wish. Here is the code:
```py
# Python code to illustrate split() function
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
```
There are also various other functions that help to manipulate the files and its contents. One can explore various other functions in Python Docs.


# Open a File in Python

Python provides inbuilt functions for creating, writing and reading files. There are two types of files that can be handled in Python, normal text files and binary files (written in binary language, 0s and 1s).

- Text files: In this type of file, Each line of text is terminated with a special character called EOL (End of Line), which is the new line character (```‘\n’```) in Python by default.
- Binary files: In this type of file, there is no terminator for a line and the data is stored after converting it into machine-understandable binary language.

## Opening a file
Opening a file refers to getting the file ready either for reading or for writing. This can be done using the open() function. This function returns a file object and takes two arguments, one that accepts the file name and another that accepts the mode(Access Mode). Now, the question arises what is access mode?

Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in python.

- **Read Only (`‘r’`):** Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exist, raises I/O error. This is also the default mode in which the file is opened.

- **Read and Write (`‘r+’`):** Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.

- **Write Only (`‘w’`):** Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.

- **Write and Read (`‘w+’`):** Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.

- **Append Only (`‘a’`):** Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

- **Append and Read (`‘a+’`):** Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Syntax:

```py
File_object = open(r"File_Name", "Access_Mode")
```
> **Note:** The file should exist in the same directory as the Python script, otherwise full address of the file should be written.

### Example 1: We want to read the content of the file using Python.
```py
# Python program to demonstrate
# opening a file
  
  
# Open function to open the file "myfile.txt"  
# (same directory) in read mode and store
# it's reference in the variable file1
  
file1 = open("myfile.txt")
  
# Reading from file
print(file1.read())
  
file1.close()
```
Output:
```
Welcome to GeeksForGeeks!!
```

### Example 2: Suppose we want to write more data to the above file using Python.
```py
# Python program to demonstrate
# opening a file
  
  
# Open function to open the file "myfile.txt"
# (same directory) in append mode and store
# it's reference in the variable file1
file1 = open("myfile.txt", "a")
  
# Writing to file
file1.write("\nWriting to file :)")
  
# Closing file
file1.close()
```

# How to read from a file in Python

## Access mode
Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. Different access modes for reading a file are –

- **Read Only (‘r’) :** Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.

- **Read and Write (‘r+’) :** Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.

- **Append and Read (‘a+’) :** Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Note: To know more about access mode click here.

## Opening a File
It is done using the open() function. No module is required to be imported for this function.



Syntax:
```py
File_object = open(r"File_Name", "Access_Mode")
```
The file should exist in the same directory as the python program file else, full address of the file should be written on place of filename.

> **Note:** The r is placed before filename to prevent the characters in filename string to be treated as special character. For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in same directory and address is not being placed.

```py
# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
file1 = open("MyFile.txt", "r") 
    
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:\Text\MyFile2.txt", "r+") 
```

Here, file1 is created as object for MyFile1 and file2 as object for MyFile2.

## Closing a file
close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode.

Syntax:
```
File_object.close()
```

```py
# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
file1 = open("MyFile.txt", "r") 
file1.close() 
```
## Reading from a file
There are three ways to read data from a text file.

- `read()` : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
```
File_object.read([n])
```

- `readline()` : Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
```
File_object.readline([n])
```

- `readlines()` : Reads all the lines and return them as each line a string element in a list.
```
File_object.readlines()
```
> **Note:** ‘\n’ is treated as a special character of two bytes.



Example:

```py
# Program to show various ways to 
# read data from a file. 
  
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
# Writing data to a file
file1.write("Hello \n") 
file1.writelines(L)
file1.close()  # to change file access modes
  
file1 = open("myfile.txt", "r+")
  
print("Output of Read function is ")
print(file1.read())
print()
  
# seek(n) takes the file handle to the nth
# bite from the beginning. 
file1.seek(0)
  
print("Output of Readline function is ")
print(file1.readline())
print()
  
file1.seek(0)
  
# To show difference between read and readline 
print("Output of Read(9) function is ")
print(file1.read(9))
print()
  
file1.seek(0)
  
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
  
file1.seek(0)
  
# readlines function 
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close() 
```

Output:
```
Output of Read function is
Hello
This is Delhi
This is Paris
This is London


Output of Readline function is
Hello


Output of Read(9) function is
Hello
Th

Output of Readline(9) function is
Hello


Output of Readlines function is
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']
```

## With statement
with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources.

Syntax:
```
with open filename as file:
```

```py
# Program to show various ways to
# read data from a file.
  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
# Creating a file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
    file1.close()  # to change file access modes
  
with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())
```

Output:
```
Hello
This is Delhi
This is Paris
This is London
```
---

# Writing to file in Python

## Access mode
Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once it’s opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. Different access modes for reading a file are –

- **Write Only (`‘w’`)** : Open the file for writing. For an existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.

- **Write and Read (`‘w+’`)** : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.

- **Append Only (`‘a’`)** : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.


## Opening a File
It is done using the open() function. No module is required to be imported for this function.

Syntax:
```
File_object = open(r"File_Name", "Access_Mode")
```
The file should exist in the same directory as the python program file else, full address of the file should be written on place of filename.

> **Note:** The r is placed before filename to prevent the characters in filename string to be treated as special character. For example, if there is \temp in the file address, then \t is treated as the tab character and error is raised of invalid address. The r makes the string raw, that is, it tells that the string is without any special characters. The r can be ignored if the file is in same directory and address is not being placed.

```py
# Open function to open the file "MyFile1.txt"  
# (same directory) in read mode and 
file1 = open("MyFile.txt", "w") 
    
# store its reference in the variable file1  
# and "MyFile2.txt" in D:\Text in file2 
file2 = open(r"D:\Text\MyFile2.txt", "w+") 
```

Here, file1 is created as object for MyFile1 and file2 as object for MyFile2.

## Closing a file
close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode.

Syntax:
```
File_object.close()
```

```py
# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
file1 = open("MyFile.txt", "w") 
file1.close() 
```

## Writing to file
There are two ways to write in a file.



- `write()` : Inserts the string str1 in a single line in the text file.
```
File_object.write(str1)
```

- `writelines()` : For a list of string elements, each string is inserted in the text file. Used to insert multiple strings at a single time.
```
File_object.writelines(L) for L = [str1, str2, str3] 
```

> **Note:** ‘\n’ is treated as a special character of two bytes.

Example:

```py
# Python program to demonstrate
# writing to file
  
# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
  
# Writing a string to file
file1.write(s)
  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()
  
# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()
```

Output:
```
Hello
This is Delhi
This is Paris
This is London
```

## Appending to a file
When the file is opened in append mode, the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data. Let’s see the below example to clarify the difference between write mode and append mode.

```py
# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()
  
# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()
  
file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
  
# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()
  
file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
```

Output:
```
Output of Readlines after appending
This is Delhi
This is Paris
This is London
Today


Output of Readlines after writing
Tomorrow
```

## With statement
with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources.

Syntax:
```
with open filename as file:
```

```py
# Program to show various ways to
# write data to a file using with statement
  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
# Writing to file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)
  
# Reading from file
with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())
```

Output:
```
Hello
This is Delhi
This is Paris
This is London
```

