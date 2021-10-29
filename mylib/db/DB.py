import sqlite3
from sqlite3 import *
import datetime


class Database:

    def __init__(self,dbName):
        self.dbName = dbName
        self.conn = None
        self.cur = None
        self.logFile = dbName+".log"
        pass

    def Connect(self):
        try:
            self.conn = sqlite3.connect(self.dbName)
            print("sql: Connected to {0} ".format(self.dbName))
        except Error as e:
            m1 = "sql: The Error '{0}' occurred".format(e)
            print(m1)
            self.log(m1)
        
        return self.conn

    def ExecuteQuery(self,query):
        self.cur = self.conn.cursor()
        result = None
        try:
            print("sql: {0}".format(query))
            self.cur.execute(query)
            result = self.cur.fetchall()
            self.conn.commit()
            return result
        except Error as e:
            print(f"sql: The error '{e}' occurred")

    def Disconnect(self):
        self.cur.close()
        self.conn.close()

    def log(self,msg):
        log = open(self.logFile,"+a")
        msgText = ("{0} | {1} \n".format(datetime.datetime.now(),msg))
        log.write(msgText)
        log.close()
        
    

