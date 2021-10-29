import sqlite3

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


i = None
while(i != ":quit"):
    i = input("[sql] ")
    
    if(i == ":quit"):
        break
    elif(i.startswith(":db")):
        dbnm = i.split("=")[1]
        con = sqlite3.connect(dbnm)
        print(f"connected to {dbnm}")
    else:
        Execute(i)
        
