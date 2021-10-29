from sqlite3.dbapi2 import Error
import DB as db
from dbmodel import *


db_name = "abc1.db"#db_mod["db_name"]
db_create_query = db_mod["db_create_query"]
db_insert_query = db_mod["db_insert_query"]



d = db.Database(db_name)
d.Connect()
#create
#res = d.ExecuteQuery(db_create_query)
#d.ExecuteQuery(db_insert_query.format("name03","vinod03"))

d.ExecuteQuery("INSERT INTO cars VALUES(1,'Audi',52642)")


select_query = "SELECT * from cars"

res = d.ExecuteQuery(select_query)

print(res)
try:
  for u in res:
    print(u)
except:
  print(res)


