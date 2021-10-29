import sys
import subprocess
import time
import os
from os import system, name
import datetime



line="\u2550"

class WatchMan(object):
   def __init__(self,file):
      self._cached_stamp = os.stat(file).st_mtime
      self.filename = file
   

   def Look(self):
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
      print ((line*15)+'#:RE-COMPILING: ' + pyfile + " #"+ (line*15))
      #print(line * 30)
      RECOMPILE(pyfile)
      self.Look()
      
   


def RECOMPILE(file):
   subprocess.run(['python.exe', file])
   print(line * 15 + "# (Ctrl + c to Stop) #" + (line * 15) )


def main(file):
   m = WatchMan(file)
   while (1==1):
      try:
         time.sleep(0.5)
         m.Look()
      except KeyboardInterrupt:
         print("Stopped by User")
         break
      except:
         print(f'Unhandled error: {sys.exc_info()[0]}')


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print("#:RE-COMPIL-ERR:# ")
print("file will be compiled on each edit")
if(len(sys.argv)-1 >= 1):
   pyfile = str(sys.argv[1])
   #delay = int(sys.argv[2])
   #DEBUG(pyfile,delay)
   main(pyfile)
else:
   pyfile = input("Enter Python file: ")
   #delay = int(input("Enter delay(miliseconds): "))
   #DEBUG(pyfile,delay)
   clear()
   print("#:RE-COMPIL-ERR:# ")
   print("file will be compiled on each edit")
   main(pyfile)






