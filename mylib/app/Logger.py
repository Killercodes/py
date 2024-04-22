import datetime
import os

os.system('')

class Logger:
    _instance = None

    @staticmethod
    def getLogger():
        if Logger._instance == None:
            Logger()
        return Logger._instance

    def __init__(self):
        x = datetime.datetime.now()
        self.logfile = x.strftime("log%Y%m%d.txt")
        if Logger._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Logger._instance = self

    def __writeLog(self,level,msg):
        x = datetime.datetime.now()
        ts = x.strftime("%H:%M:%S.%f")
        format = f"{ts}|{level}|{msg}\n"
        f = open(self.logfile, "a")
        f.write(format)
        f.close()

    def __rgb(self,value=None,bg=False):
        if(value==None):
            return '\u001b[0m'
        
        value = value.replace('#','')#value.lstrip('#')
        lv = len(value)
        rgb = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        if(bg==False):
            return f'\u001b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m'
        elif(bg==True):
            return f'\u001b[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m'

    def info(self,msg):
        self.__writeLog("INFO",msg)
        cyan = self.__rgb("#00FFF7")
        default = self.__rgb()
        print(f"{cyan}[!] {msg}{default}")
    
    def warn(self,msg):
        self.__writeLog("WARN",msg)
        print(f"[#] {msg}")

    def error(self,msg):
        self.__writeLog("EROR",msg)
        print(f"[X] {msg}")

# Create a new instance
l1 = Logger.getLogger()
l1.info("This is an info")

# Try to create another instance
l2 = Logger.getLogger()
l2.error("Thsi s an error ")

