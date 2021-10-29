import os
import sys

os.system('')

def rgb(red, green, blue):
  return f'\x1b[38;2;{red};{green};{blue}m'

def fg8(red, green, blue):
  return f'\x1b[38;5;{red};{green};{blue}m'


def fg(ccode):
  return f"\u001b[38;5;{ccode}m "

def bg(ccode):
  return f"\u001b[48;5;{ccode}m "

def nc():
  return "\u001b[0m"

def bt():
  return "\u001b[1m"

def ut():
  return "\u001b[4m"

def rt():
  return "\u001b[7m"



red_color = rgb(255, 0, 0)
red_green = rgb(25,255,0)
green_color = rgb(50, 255, 100)
blue_color = rgb(0, 0, 255)

def main():
  print(f'{red_color}red {green_color}green {blue_color}blue {red_green} regreen')
  #print(bg(40) +fg(0) + bt() +"col "+nc())
  print(nc())
  for v in range(0,255):
    c = fg(v)
    t = bg(v)
    i = rt()
    n = nc()
    print(f'{c}fore color {v} {n}')
    print(f'{t}back color {v} {n}')
    #print(nc())

'''
  print ("FOREGROUND")
  for i in range(0, 16):
      for j in range(0, 16):
          code = str(i * 16 + j)
          #sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
          print(u"\u001b[38;5;" + code + "m " + code.ljust(4),end=" ")
          #print(u"\u001b[44;5;" + code + "m " + code.ljust(4))
      print(u"\u001b[0m")

  print("BACKGROUND")
  for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        #sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")
'''

class Console:
        """ color class"""
        
        def Foreground(col,txt):
                return(f"\u001b[38;5;{col}m {txt}\u001b[0m")
                

        @staticmethod
        def fgcolor(code):
                return(f"\u001b[38;2;{code}m ")

        @staticmethod
        def bgcolor(code):
                return(f"\u001b[48;2;{code}m ")
        
        @staticmethod
        def nocolor():
                return("\u001b[0m")
        
        @staticmethod
        def bold():
                return("\u001b[1m")
        
        @staticmethod
        def underline():
                return("\u001b[4m")

        @staticmethod
        def invert():
                return("\u001b[7m")

        @staticmethod
        def hr():
                return("\u2550")
                
class UI:
        @staticmethod
        def loading(i):
                for i in range(0, 101):
                        time.sleep(0.05)
                        print("\u2592"* int(i/4) + f" Loading {i}% \u2592",end="\r")
                        #sys.stdout.flush()
                print()

        @staticmethod
        def title(string):
                string = str(string)
                fcolor = "\u001b[38;2;255;200;0m"
                bcolor = "\u001b[48;5;235m"
                nocolor = "\u001b[0m"
                l="\u2550"
                slen = len(string)
                l= l*(slen +0)
                print(f"{fcolor}{bcolor}\u2554{l}\u2557")   
                print(f"\u2551{bcolor}"+string +f"\u2551{nocolor}")
                print(f"{fcolor}{bcolor}\u255A{l}\u255D{nocolor}") 
        
        @staticmethod
        def prompt(msg):
                i = input("\u001b[48;5;235m [?] " + msg + ": \u001b[0m ")
                return i

        @staticmethod
        def printx(msg):
                print("\u001b[48;5;235m" + msg + ": \u001b[0m")

class Cursor:
        @staticmethod
        def up():
                return("\u001b[{n}A")

        @staticmethod
        def down():
                return("\u001b[{n}B")
        
        @staticmethod
        def right():
                return("\u001b[{n}C")
        
        @staticmethod
        def left():
                return("\u001b[{n}D")
        

def rainbow255():
    for r in range(0,255):
        print(f'\x1b[38;2;{r};0;0m \x1b[48;5;235m color {r} \u001b[0m')

    

def rainbow16():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            #sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
            print(u"\x1b[48;5;234m \u001b[38;5;" + code + "m " + code.ljust(4),end=" ")
            #print(u"\u001b[44;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")

def rainbowBG():
    print("BACKGROUND")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            #sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
            print(u"\u001b[48;5;" + code + "m \u001b[38;5;1m" + code.ljust(4))
        print(u"\u001b[0m")




if __name__ == "__main__":
  main()


