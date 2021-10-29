import sys
import subprocess
import time
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()


line="\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550"


class Monkey(object):
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

         
   
   def Run(self):
      print (Fore.LIGHTWHITE_EX+'#:RE-COMPILING:# ' + pyfile)
      print(line)
      print(Style.RESET_ALL)
      RECOMPILE(pyfile)
      self.Look()
   


def DEBUG(pyfile,delay):
   print("Compiling: {0} every {1} second".format(pyfile,delay))
   while (1==1):
      
      print (Fore.LIGHTWHITE_EX+'#:RE-COMPILING:# ' + pyfile)
      print(line)
      print(Style.RESET_ALL)
      RECOMPILE(pyfile)
      time.sleep(delay)

def RECOMPILE(file):
   print(Fore.LIGHTCYAN_EX)
   subprocess.run(['python.exe', file])
   print(Style.RESET_ALL)
   print(line)


if(len(sys.argv)-1 >= 1):
   pyfile = str(sys.argv[1])
   delay = int(sys.argv[2])
   #DEBUG(pyfile,delay)
   m = Monkey(pyfile)
   m.Look()
else:
   pyfile = input("Enter Python file: ")
   delay = int(input("Enter delay(miliseconds): "))
   #DEBUG(pyfile,delay)

   m = Monkey(pyfile)
   while (1==1):
      try:
         time.sleep(1)
         m.Look()
      except KeyboardInterrupt:
         print("Stopped")
         break
      except:
         print(f'Unhandled error: {sys.exc_info()[0]}')


