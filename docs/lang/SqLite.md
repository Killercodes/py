# SQLite with Python
SQLite is probably the most straightforward database to connect to with a Python application since you don’t need to install any external Python SQL modules to do so. By default, your Python installation contains a Python SQL library named sqlite3 that you can use to interact with an SQLite database.

## Connecting to SQLite
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
