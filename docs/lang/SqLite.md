# SQLite with Python
SQLite is probably the most straightforward database to connect to with a Python application since you don’t need to install any external Python SQL modules to do so. By default, your Python installation contains a Python SQL library named sqlite3 that you can use to interact with an SQLite database.


## Connecting to SQLite
```py
import sqlite3
import sys
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        sys.exit(1)

    return connection
```

## Using `With` keyword
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")
```


## Creating Tables 
To execute queries in SQLite, use `cursor.execute()`. In this section, you’ll define a function execute_query() that uses this method. Your function will accept the connection object and a query string, which you’ll pass to `cursor.execute()`.

`.execute()` can execute any query passed to it in the form of string. You’ll use this method to create tables in this section. In the upcoming sections, you’ll use this same method to execute update and delete queries as well.

```py
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

execute_query(connection, create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
execute_query(connection, create_posts_table)

```
You can see that creating tables in SQLite is very similar to using raw SQL. All you have to do is store the query in a string variable and then pass that variable to `cursor.execute()`.

## create_table.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars;")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',21600)")
```

## create_table2.py
```py
#!/usr/bin/python

import sqlite3

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
```


## Inserting Records into TABLE
To insert records into your SQLite database, you can use the same execute_query() function that you used to create tables. First, you have to store your INSERT INTO query in a string. Then, you can pass the connection object and query string to execute_query(). Let’s insert five records into the users table:

```py
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)  

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

execute_query(connection, create_posts)
```


## Selecting Records
To select records using SQLite, you can again use cursor.execute(). However, after you’ve done this, you’ll need to call .fetchall(). This method returns a list of tuples where each tuple is mapped to the corresponding row in the retrieved records.

```py
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
```

### SELECT
Let’s now select all the records from the users table:

```py
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)
```
**Output:**
```
(1, 'James', 25, 'male', 'USA')
(2, 'Leila', 32, 'female', 'France')
(3, 'Brigitte', 35, 'female', 'England')
(4, 'Mike', 40, 'male', 'Denmark')
(5, 'Elizabeth', 21, 'female', 'Canada')
```


In the above script, the SELECT query selects all the users from the users table. This is passed to the execute_read_query(), which returns all the records from the users table. The records are then traversed and printed to the console.

### JOIN
You can also execute complex queries involving JOIN operations to retrieve data from two related tables. For instance, the following script returns the user ids and names, along with the description of the posts that these users posted:

```py
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""

users_posts = execute_read_query(connection, select_users_posts)

for users_post in users_posts:
    print(users_post)
```
**Output;**
```
(1, 'James', 'I am feeling very happy today')
(2, 'Leila', 'The weather is very hot today')
(2, 'Leila', 'I need some help with my work')
(1, 'James', 'I am getting married')
(5, 'Elizabeth', 'It was a fantastic game of tennis')
(3, 'Brigitte', 'Anyone up for a late night party today?')
```

You can see from the output that the column names are not being returned by .fetchall(). To return column names, you can use the .description attribute of the cursor object.

```py
cursor = connection.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)
```

### WHERE
Now you’ll execute a SELECT query that returns the post, along with the total number of likes that the post received:

```py
select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""

post_likes = execute_read_query(connection, select_post_likes)

for post_like in post_likes:
    print(post_like)
```
**Output:**
```
('The weather is very hot today', 1)
('I need some help with my work', 1)
('I am getting married', 2)
('It was a fantastic game of tennis', 1)
('Anyone up for a late night party today?', 2)
```

## Updating Table Records
Updating records in SQLite is pretty straightforward. You can again make use of execute_query(). As an example, you can update the description of the post with an id of 2. First, SELECT the description of this post:

```py
select_post_description = "SELECT description FROM posts WHERE id = 2"

post_description = execute_read_query(connection, select_post_description)

for description in post_description:
    print(description)
```
**Output:**
```
('The weather is very hot today',)
```

The following script updates the description:
```py
update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection, update_post_description)
```
**Output:**
```
('The weather has become pleasant now',)
```

## Deleting Table Records
You can again use `execute_query()` to delete records from YOUR SQLite database. All you have to do is pass the connection object and the string query for the record you want to delete to `execute_query()`. Then, `execute_query()` will create a cursor object using the connection and pass the string query to `cursor.execute()`, which will delete the records.

```py
delete_comment = "DELETE FROM comments WHERE id = 5"
execute_query(connection, delete_comment)
```

----

# SQLite Examples

## Python SQLite version example
In the first code example, we will get the version of the SQLite database.

### version.py
```py
#!/usr/bin/python

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")

except sqlite3.Error as e:

    print(f"Error {e.args[0]}")
    sys.exit(1)

finally:

    if con:
        con.close()
```
In the above Python script we connect to the previously created ydb.db database. We execute an SQL statement which returns the version of the SQLite database.
```py
import sqlite3
```
We import the sqlite3 module.
```py
con = None
```
We initialise the con variable to None. In case we could not create a connection to the database (for example the disk is full), we would not have a connection variable defined. This would lead to an error in the finally clause.
```py
con = sqlite3.connect('ydb.db')
```
We connect to the ydb.db database. The connect method returns a connection object.
```py
cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION()')
```
From the connection, we get the cursor object. The cursor is used to traverse the records from the result set. We call the execute method of the cursor and execute the SQL statement.
```py
data = cur.fetchone()[0]
```
We fetch the data. Since we retrieve only one record, we call the fetchone method.
```py
print(f"SQLite version: {data}")
```
We print the data that we have retrieved to the console.
```py
except sqlite3.Error as e:

    print(f"Error {e.args[0]}")
    sys.exit(1)
```
In case of an exception, we print an error message and exit the script with an error code 1.

```py
finally:

    if con:
        con.close()
```
In the final step, we release the resources.

In the second example, we again get the version of the SQLite database. This time we will use the with keyword.

### version2.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f"SQLite version: {data}")
```
The script returns the current version of the SQLite database. With the use of the with keyword. The code is more compact.
```py
with con:
```
With the with keyword, the Python interpreter automatically releases the resources. It also provides error handling.
```
$ ./version2.py
SQLite version: 3.33.0
```
This is the output.

## Python SQLite execute
We create a cars table and insert several rows to it. We use execute.

### create_table.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars;")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',21600)")
```
The above script creates a cars table and inserts eight rows into the table.
```py
cur.execute("DROP TABLE IF EXISTS cars;")
```
We drop the table if it already exists.
```py
cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
```
This SQL statement creates a new cars table. The table has three columns.
```py
cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
```
These two lines insert two cars into the table. Using the with keyword, the changes are automatically committed. Otherwise, we would have to commit them manually.
```
sqlite> .mode column
sqlite> .headers on
```


## Python SQLite executemany
We are going to create the same table. This time using the convenience executemany method.

### create_table2.py
```py
#!/usr/bin/python

import sqlite3

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
```

The program drops the cars table if it exists and recreates it.
```py
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
```
The first SQL statement drops the cars table if it exists. The second SQL statement creates the cars table.
```py
cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
```
We insert eight rows into the table using the convenience executemany method. The first parameter of this method is a parameterized SQL statement. The second parameter is the data, in the form of tuple of tuples.

## Python SQLite executescript
We provide another way to create our cars table with executescript. We commit the changes manually and provide our own error handling.

### create_table3.py
```py
#!/usr/bin/python

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS cars;
        CREATE TABLE cars(id INT, name TEXT, price INT);
        INSERT INTO cars VALUES(1,'Audi',52642);
        INSERT INTO cars VALUES(2,'Mercedes',57127);
        INSERT INTO cars VALUES(3,'Skoda',9000);
        INSERT INTO cars VALUES(4,'Volvo',29000);
        INSERT INTO cars VALUES(5,'Bentley',350000);
        INSERT INTO cars VALUES(6,'Citroen',21000);
        INSERT INTO cars VALUES(7,'Hummer',41400);
        INSERT INTO cars VALUES(8,'Volkswagen',21600);
        """)

    con.commit()

except sqlite3.Error as e:

    if con:
        con.rollback()

    print(f"Error {e.args[0]}")
    sys.exit(1)

finally:

    if con:
        con.close()
```
In the above script we (re)create the cars table using the executescript method.
```py
cur.executescript("""
    DROP TABLE IF EXISTS cars;
    CREATE TABLE cars(id INT, name TEXT, price INT);
    INSERT INTO cars VALUES(1,'Audi',52642);
    INSERT INTO cars VALUES(2,'Mercedes',57127);
...
```
The executescript method allows us to execute the whole SQL code in one step.
```py
con.commit()
```
Without the with keyword, the changes must be committed using the commit method.
```py
except sqlite.Error as e:

    if con:
        con.rollback()

    print(f"Error {e.args[0]}")
    sys.exit(1)
```
In case of an error, the changes are rolled back and an error message is printed to the terminal.


## Python SQLite check database existence
It is not possible to check the existence of the database file using the connect method. The method simply connects to the database, if the given file exists. If it does not exist, the database file is created. The existence of the database file can be checked with the standard os.path.exist function.

### db_exists.py
```py
#!/usr/bin/python

import os
import sqlite3


if not os.path.exists('ydb.db'):

    con = sqlite3.connect('ydb.db')

    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS cars")
        cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
        cur.execute("INSERT INTO cars VALUES(1,'Audi', 52642)")
        cur.execute("INSERT INTO cars VALUES(2,'Mercedes', 57127)")
        cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO cars VALUES(5,'Bentley', 350000)")
        cur.execute("INSERT INTO cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO cars VALUES(8,'Volkswagen', 21600)")

else:

    con = sqlite3.connect('ydb.db')

    with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM cars")
        rows = cur.fetchmany(2)

        print(rows)
```
In the script we check for the existence of the ydb.db file. If it does not exist, it is created and a new table is generated. If it already exists, we retrieve two rows from the table.
```py
if not os.path.exists('test.db'):

  con = sqlite3.connect('test.db')
  ...
```
We check for the existence of the ydb.db file using the os.path.exists method. The database file is created if it does not exist.
```py
else:

  con = sqlite3.connect('ydb.db')
  ...
```
If the database file already exists, we connect to it and later fetch some data.


## Python SQLite lastrowid
Sometimes, we need to determine the id of the last inserted row. In Python SQLite, we use the lastrowid attribute of the cursor object.

### lastrowid.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect(':memory:')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom');")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim');")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert');")

    last_row_id = cur.lastrowid

    print(f"The last Id of the inserted row is {last_row_id}")
```
We create a friends table in memory. The Id is automatically incremented.
```py
cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT);")
```
In SQLite, INTEGER PRIMARY KEY column is auto incremented. There is also an AUTOINCREMENT keyword. When used in INTEGER PRIMARY KEY AUTOINCREMENT a slightly different algorithm for Id creation is used.
```py
cur.execute("INSERT INTO friends(name) VALUES ('Tom');")
cur.execute("INSERT INTO friends(name) VALUES ('Rebecca');")
cur.execute("INSERT INTO friends(name) VALUES ('Jim');")
cur.execute("INSERT INTO friends(name) VALUES ('Robert');")
```
When using auto-increment, we have to explicitly state the column names, omitting the one that is auto-incremented. The four statements insert four rows into the friends table.
```py
last_row_id = cur.lastrowid
```
Using the lastrowid we get the last inserted row id.

## Python SQLite retrieve data with fetchall
The fetchall method fetches all (or all remaining) rows of a query result set and returns a list of tuples.

### fetch_all.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]}")
```
In this example, we retrieve all data from the cars table.
```py
cur.execute("SELECT * FROM cars")
```
This SQL statement selects all data from the cars table.
```py
rows = cur.fetchall()
```
The fetchall method gets all records. It returns a result set. Technically, it is a tuple of tuples. Each of the inner tuples represent a row in the table.

```py
for row in rows:
    print(f"{row[0]} {row[1]} {row[2]}")
```    
We print the data to the console, row by row.


## Python SQLite fetchone
The fetchone returns the next row of a query result set, returning a single tuple, or None when no more data is available.

### fetch_one.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    while True:

        row = cur.fetchone()

        if row == None:
            break

        print(f"{row[0]} {row[1]} {row[2]}")
```

In this script we connect to the database and fetch the rows of the cars table one by one.
```py
while True:
```
We access the data from the while loop. When we read the last row, the loop is terminated.
```py
row = cur.fetchone()

if row == None:
    break
```
The fetchone method returns the next row from the table. If there is no more data left, it returns None. In this case we break the loop.
```py
print(f"{row[0]} {row[1]} {row[2]}")
```
The data is returned in the form of a tuple. Here we select records from the tuple. The first is the Id, the second is the car name and the third is the price of the car.

## Python SQLite dictionary cursor
The default cursor returns the data in a tuple of tuples. When we use a dictionary cursor, the data is sent in the form of Python dictionaries. This way we can refer to the data by their column names.

### dictionary_cursor.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row['id']} {row['name']} {row['price']}")
```

In this example, we print the contents of the cars table using the dictionary cursor.
```py
con.row_factory = sqlite.Row
```
We select a dictionary cursor. Now we can access records by the names of columns.
```py
for row in rows:
    print(f"{row['id']} {row['name']} {row['price']}")
```
The data is accessed by the column names.


# Python SQLite parameterized statements
Now we will concern ourselves with parameterized queries. When we use parameterized queries, we use placeholders instead of directly writing the values into the statements. Parameterized queries increase security and performance.

The Python `sqlite3` module supports two types of placeholders: question marks and named placeholders.

## Parameterized statements with question marks
In the first example we use the syntax of question marks.

### parameterized_query.py
```py
#!/usr/bin/python

import sqlite3

uId = 1
uPrice = 62300

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    print(f"Number of rows updated: {cur.rowcount}")
```
We update a price of one car. In this code example, we use the question mark placeholders.
```py
cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))
```
The question marks ? are placeholders for values. The values are added to the placeholders.
```py
print(f"Number of rows updated: {cur.rowcount}")
```
The rowcount property returns the number of updated rows. In our case one row was updated.


## Parameterized statements with named placeholders
The second example uses parameterized statements with named placeholders.

### named_placeholders.py
```py
#!/usr/bin/python

import sqlite3

uId = 4

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name, price FROM cars WHERE Id=:Id", {"Id": uId})

    row = cur.fetchone()
    print(f"{row[0]}, {row[1]}")
```
We select a name and a price of a car using named placeholders.
```py
cur.execute("SELECT name, price FROM cars WHERE Id=:Id", {"Id": uId})
```
The named placeholders start with a colon character.

# Python SQLite Image 

## Python SQLite insert image
In this section, we are going to insert an image to the SQLite database. Note that some people argue against putting images into databases. Here we only show how to do it. We do not dwell into technical issues of whether to save images in databases or not.
```
sqlite> CREATE TABLE images(id INTEGER PRIMARY KEY, data BLOB);
```
For this example, we create a new table called images. For the images, we use the BLOB data type, which stands for Binary Large Objects.

### insert_image.py
```py
#!/usr/bin/python

import sqlite3
import sys

def readImage():

    fin = None

    try:
        fin = open("sid.jpg", "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fin:
            fin.close()

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()

    data = readImage()
    binary = sqlite3.Binary(data)
    cur.execute("INSERT INTO images(data) VALUES (?)", (binary,) )

    con.commit()

except sqlite3.Error as e:

    if con:
        con.rollback()

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
```
In this script, we read an image from the current working directory and write it into the images table of the SQLite ydb.db database.
```py
try:
    fin = open("sid.jpg", "rb")
    img = fin.read()
    return img
```
We read binary data from the filesystem. We have a JPG image called sid.jpg.
```py
binary = sqlite3.Binary(data)
```
The data is encoded using the SQLite Binary object.
```py
cur.execute("INSERT INTO images(data) VALUES (?)", (binary,) )
```
This SQL statement is used to insert the image into the database.


## Python SQLite read image
In this section, we are going to perform the reverse operation: we read an image from the database table.

### read_image.py
```py
#!/usr/bin/python

import sqlite3
import sys


def writeImage(data):

    fout = None

    try:
        fout = open('sid2.jpg','wb')
        fout.write(data)

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fout:
            fout.close()

con = None

try:
    con = sqlite3.connect('ydb.db')

    cur = con.cursor()
    cur.execute("SELECT data FROM images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)


except sqlite3.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
```
We read image data from the images table and write it to another file, which we call sid2.jpg.

```py
try:
    fout = open('sid2.jpg','wb')
    fout.write(data)
```
We open a binary file in a writing mode. The data from the database is written to the file.
```py
cur.execute("SELECT data FROM images LIMIT 1")
data = cur.fetchone()[0]
```
These two lines select and fetch data from the images table. We obtain the binary data from the first row.

# Python SQLite metadata
Metadata is information about the data in the database. Metadata in a SQLite contains information about the tables and columns, in which we store data. Number of rows affected by an SQL statement is a metadata. Number of rows and columns returned in a result set belong to metadata as well.

Metadata in SQLite can be obtained using the PRAGMA command. SQLite objects may have attributes, which are metadata. Finally, we can also obtain specific metatada from querying the SQLite system sqlite_master table.

### column_names.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()

    cur.execute('PRAGMA table_info(cars)')

    data = cur.fetchall()

    for d in data:
        print(f"{d[0]} {d[1]} {d[2]}")
```

In this example, we issue the PRAGMA table_info(tableName) command, to get some metadata info about our cars table.
```py
cur.execute('PRAGMA table_info(cars)')
```
The PRAGMA table_info(tableName) command returns one row for each column in the cars table. Columns in the result set include the column order number, column name, data type, whether or not the column can be NULL, and the default value for the column.
```py
for d in data:
    print(f"{d[0]} {d[1]} {d[2]}")
```
From the provided information, we print the column order number, column name and column data type.
```
$ ./column_names.py
0 id INT
1 name TEXT
2 price INT
```

In the following example we print all rows from the cars table with their column names.

### column_names2.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute('SELECT * FROM cars')

    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print(f"{col_names[0]:3} {col_names[1]:10} {col_names[2]:7}")

    for row in rows:
        print(f"{row[0]:<3} {row[1]:<10} {row[2]:7}")
```
We print the contents of the cars table to the console. Now, we include the names of the columns too. The records are aligned with the column names.
```py
col_names = [cn[0] for cn in cur.description]
```
We get the column names from the description property of the cursor object.
```py
print(f"{col_names[0]:3} {col_names[1]:10} {col_names[2]:7}")
```
This line prints three column names of the cars table.
```py
for row in rows:
    print(f"{row[0]:<3} {row[1]:<10} {row[2]:7}")
```
We print the rows using the for loop. The data is aligned with the column names.

In our last example related to the metadata, we will list all tables in the ydb.db database.

### list_tables.py
```py
#!/usr/bin/python

import sqlite3

con = sqlite3.connect('ydb.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])
```
The code example prints all available tables in the current database to the terminal.
```py
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
```
The table names are stored inside the system sqlite_master table.
```
$ ./list_tables.py
cars
images
```

# Python SQLite data export
We can dump data in an SQL format to create a simple backup of our database tables.

### export_table.py
```py
#!/usr/bin/python

import sqlite3

cars = (
    (1, 'Audi', 52643),
    (2, 'Mercedes', 57642),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

def writeData(data):

    f = open('cars.sql', 'w')

    with f:
        f.write(data)


con = sqlite3.connect(':memory:')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
    cur.execute("DELETE FROM cars WHERE price < 30000")

    data = '\n'.join(con.iterdump())

    writeData(data)
```
In the above example, we recreate the cars table in the memory. We delete some rows from the table and dump the current state of the table into a cars.sql file. This file can serve as a current backup of the table.

```py
def writeData(data):

    f = open('cars.sql', 'w')

    with f:
        f.write(data)
```

The data from the table is being written to the file.
```py
con = sqlite3.connect(':memory:')
```
We create a temporary table in the memory.
```py
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
cur.execute("DELETE FROM cars WHERE price < 30000")
```
These lines create a cars table, insert values and delete rows, where the price is less than 30000 units.
```py
data = '\n'.join(con.iterdump())
```
The `con.iterdump()` returns an iterator to dump the database in an SQL text format. The built-in join function takes the iterator and joins all the strings in the iterator separated by a new line. This data is written to the `cars.sql` file in the `writeData` function.

# Python SQLite import data
Now we are going to perform a reverse operation. We will import the dumped table back into memory.

### import_table.py
```py
#!/usr/bin/python

import sqlite3


def readData():

    f = open('cars.sql', 'r')

    with f:

        data = f.read()

        return data


con = sqlite3.connect(':memory:')

with con:

    cur = con.cursor()

    sql = readData()
    cur.executescript(sql)

    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)
```
In this script, we read the contents of the cars.sql file and execute it. This will recreate the dumped table.
```py
def readData():

    f = open('cars.sql', 'r')

    with f:

        data = f.read()

        return data
```
Inside the readData() method we read the contents of the cars.sql table.
```py
cur.executescript(sql)
```
We call the executescript method to launch the SQL script.
```py
cur.execute("SELECT * FROM cars")

rows = cur.fetchall()

for row in rows:
    print(row)
```
We verify the data.
```
$ ./import_table.py
(1, 'Audi', 52643)
(2, 'Mercedes', 57642)
(5, 'Bentley', 350000)
(6, 'Hummer', 41400)
```


# Python SQLite transactions
A transaction is an atomic unit of database operations against the data in one or more databases. The effects of all the SQL statements in a transaction can be either all committed to the database or all rolled back.

Python `sqlite3` module by default issues a `BEGIN` statement implicitly before a Data Modification Language (DML) statement (i.e. `INSERT/UPDATE/DELETE/REPLACE`).

The `sqlite3` used to implicitly commit an open transaction before DDL statements. This is no longer the case.

Manual transactions are started with the `BEGIN TRANSACTION` statement and finished with the `COMMIT` or `ROLLBACK` statements.

SQLite supports three non-standard transaction levels: `DEFERRED`, `IMMEDIATE` and `EXCLUSIVE`. Python SQLite module also supports an autocommit mode, where all changes to the tables are immediately effective.

### no_commit.py
```py
#!/usr/bin/python

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('ydb.db')
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS friends")
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")

    #con.commit()

except sqlite3.Error as e:

    if con:
        con.rollback()

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
```
We create a friends table and try to fill it with data. However, as we will see, the data is not committed.
```py
#con.commit()
```
The commit method is commented. If we uncomment the line, the data will be written to the table.

## Python SQLite autocommit
In the autocommit mode, an SQL statement is executed immediately.

### autocommit.py
```py
#!/usr/bin/python

import sqlite3
import sys

con = None

try:
    con = sqlite3.connect('ydb.db', isolation_level = None)
    
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS friends")
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO friends(name) VALUES ('Tom')")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim')")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert')")

except sqlite3.Error as e:

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()
```
In this example, we connect to the database in the autocommit mode.
```py
con = sqlite3.connect('ydb.db', isolation_level = None)
```
We have an autocommit mode, when we set the isolation_level to None.
