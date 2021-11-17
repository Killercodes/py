import sys
import subprocess
import time
import os
from os import system, name
import datetime

line="\u2550"

class AutoExec(object):
    def __init__(self,file):
        self._cached_stamp = os.stat(file).st_mtime
        self.filename = file
   

    def LookForUpdate(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            self.Run()
        else:
            pass
            #print(" [{1}] Waiting for {0} edit".format(self.filename,datetime.datetime.now()), end = "\r")
         
   
    def Run(self):
        clear()
        print ((line*15)+'#:AUTO-EXECUTE: "' + pyfile + '" #'+ (line*15))
        self.ReCompile(pyfile)
        self.LookForUpdate()
    
    def Execute(file):
        m = AutoExec(file)
        while (True):
            try:
                time.sleep(1)
                m.LookForUpdate()
            except KeyboardInterrupt:
                print(" [x] Stopped by User")
                break
            except:
                print(f'Unhandled error: {sys.exc_info()[0]}')
   
    def ReCompile(self,file):
        subprocess.run(['python.exe', file])
        print(line * 15 + "# (Ctrl + c to Stop) #" + (line * 15) )


def main(file):
    AutoExec.Execute(file)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def showBanner():
    clear()
    print("#:AUTO-EXECUTE# file will be compiled on each edit")

# Execution
showBanner()
if(len(sys.argv)-1 >= 1):
   pyfile = str(sys.argv[1])
   main(pyfile)
else:
   pyfile = input("Enter Python file: ")
   clear()
   showBanner()
   main(pyfile)

  
  
