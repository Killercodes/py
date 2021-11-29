# Pinger
import os
import platform
from datetime import datetime
from mylib.Console import *

c = Console()

green=c.fgcolor("0;255;0")
b1=c.bgcolor("30;30;30")
d1 = c.fgcolor("255;100;0") + c.bgcolor("0;0;0")
u = c.underline()
nc = c.nocolor()
line = c.hr() * 50

print("\u001b[48;5;235m")

def title(string):
    string = str(string)
    fcolor = "\u001b[38;2;255;200;0m"
    bcolor = "\u001b[48;5;235m"
    nocolor = "\u001b[0m"
    l="\u2550"
    slen = len(string)
    l= l*(slen +0)
    print(bcolor)
    print(f"{fcolor}\u2554{l}\u2557")   
    print(f"\u2551"+string +f"\u2551")
    print(f"{fcolor}\u255A{l}\u255D") 

title("        \u2995  Ping-alive  \u2996        ")

def prompt(msg):
    i = input("\u001b[48;5;235m [?] " + msg + ": \u001b[0m ")
    return i

def printx(msg):
    print("\u001b[48;5;235m" + msg + ": \u001b[0m")


#print(f"{u} underline {d1} {nc}")

net = input(" [?] Enter the Network Address xxx.xxx.xxx ")
net1= net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(input(" [?] Enter the Starting Node "))
en1 = int(input(" [?] Enter the Last Node "))

en1=en1+1
oper = platform.system()
if (oper=="Windows"):
    ping1 = "ping -n 1 "
elif (oper== "Linux"):
    ping1 = "ping -c 1 "
else :
    ping1 = "ping -c 1 "
    
t1= datetime.now()
print("Scanning in Progress")

for ip in range(st1,en1):
    addr = net2+str(ip)
    print(" [+] Scanning " + addr,end="\r")
    comm = ping1+addr
    response = os.popen(comm)
    for line in response.readlines():
        if (line.count("TTL")):
            print(" [~]",addr, "--> Live")
            break
        
        
t2= datetime.now()
total =t2-t1
print(" [x] scanning complete in " , total, nc)
