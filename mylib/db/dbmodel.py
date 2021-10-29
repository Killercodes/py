
db_mod = {
    "db_name": "db3.sqlite",
    "db_table": "users",
    "db_create_query":""" 
CREATE TABLE IF NOT EXISTS kv (
  name TEXT NOT NULL,
  value TEXT NOT NULL
);
""",
"db_insert_query":"insert into kv (name, value) VALUES ('{0}','{1}')"
}

