import sqlite3


"""
SQLite client for console
"""

con = sqlite3.connect("abc1.db")
cur = con.cursor()

def Execute(cmd):
    try:
            #con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(i)
            result = cur.fetchall()
            for r in result:
                print(r)
            con.commit()
    except sqlite3.Error as e:
        if con:
            con.rollback()

        print(f"Error {e.args[0]}")

  
def Help():
    print("sql-client - commands")
    print(":hlp - print this help message")
    print(":quit - will close the connection")
    print(":db=<filename> - connect to database with <filename>")

i = None
while(i != ":quit"):
    i = input("[sql] ")
    
    if(i == ":quit"):
        print("[sql] The connection is now closed")
        break
    elif(i.startswith(":db")):
        dbnm = i.split("=")[1]
        con = sqlite3.connect(dbnm)
        print(f"[sql] Client connected to {dbnm}")
    elif(i.startswith(":help")):
        Help()
    else:
        Execute(i)
        
