import subprocess
import itertools
import string
import os
import platform
from random import *
import time
import multiprocessing


def sevenZ(zipname, password):
    try:
        #print("Testing Password : {}".format(password),end="\r")
        system = subprocess.Popen([ r"C:\Program Files\7-Zip\7z.exe", "l", zipname, "-p{}".format(password)],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output = system.communicate()
        if(output[1]==b''):
            return True
            #print("OK",password,system.communicate()[1])
        else:
            return False
            #print("ERROR",password,system.communicate()[1])
        
    except Exception as e:
        print("ERROR",type(e),e)
    
def sevenUp(zipname, password):
    try:
        print("Testing Password : {}".format(password))
        svn = "C:\Program Files\\7-Zip\\7z.exe"
        comm = (f'"{svn}" l "{zipname}" -p{password}')
        #print(comm)
        response = os.popen(comm)
        c=0
        
        #print(response)
        for line in response.readlines():
            #print(f"[{c}] => {line}")
            if (line.count("Errors")):
                #print("==> Error")
                return False
            else:
                pass
            c+= 1
        return True
            
    except Exception as e:
        print("ERROR REPORT",type(e))
        return False


def BForce(real):
    then = time.time()
    chars = string.ascii_lowercase + " " +string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            now = now = time.time() - then
            seconds = int(now % 60)
            try:
                print(guess, attempts,"at ",seconds, " seconds",end="\n")
            except:
                pass

def BrutForce(maxLen,useRandom=False, chars=None):

       
    if(chars == None):
        chars = string.ascii_lowercase +"#_"+string.digits
    print(" :BRUTFORCER:")
    mlen = len(chars)
    mlen = mlen -1
    print(" DictionarySize: ",mlen)
    print(" CharSet: ", chars)
    print(" MaxLength : ",maxLen)
    print(" UseRandom :",useRandom)
    
        
    if(useRandom == False):
        for password_length in range(0, maxLen+1):
            for s in itertools.product(chars, repeat=password_length):
                guess = ''.join(s)
                yield guess
    else:
        
        while(True):
            try:
                guess = ""
                prem = ""
                for n in range(maxLen):
                    guessletter = chars[randint(0, mlen)]
                    guess = guess + str(guessletter)
                    perm = itertools.permutations(guess)
                    
                for p in perm:                       
                    guess = "".join(p)
                    yield guess
            except Exception as e:
                break

def Timer(then):
    now = time.time() - then
    seconds = int(now % 60)
    yield seconds


def P1(t):
    print("P1")

def P2(t):
    print("P2")
    
c=0
#print(BruteForce('vin'))
#print(sevenZ("data.7z","vin"))
then = time.time()
secPlus = 0

##while(True):
t2 = time.time() - then
t2 = int(t2)
##    if(t2 == 59):
##        print("1 Min", t2, " second")
##    else:
##        print(t2, " second")

    # creating processes
p1 = multiprocessing.Process(target=P1, args=(t2,))
p2 = multiprocessing.Process(target=P2, args=(t2,))

p1.start()
p1.join()
p2.start()


p2.join()

    

        
"""
for bf in BrutForce(3,True):

    result = sevenZ("data.7z",bf)
    sec = int(next(Timer(then)))
    if(sec >= 59):
        secPlus = int(secPlus) + sec
    else:
        secPlus = sec
        
    if result == True:
        print(f"   Password is ==> '{pswd}'")
    else:
        print(f" Running.. {secPlus} seconds Testing {bf}",end="\r")
"""
"""
for bf in BrutForce(3):
    result = sevenZ("data.7z",bf)
    if result == True:
        print(f"   Password is ==> '{pswd}'")
"""
"""
for e in sevenZ("data.7z","vind"):
    print(c," ==> " ,e)
    c+=1
"""    

"""
wordlist = itertools.permutations("niv")
for w in wordlist:
    #result = sevenUp("data.7z",w)
    pswd = "".join(w)
    result = sevenZ("data.7z",pswd)
    if result == True:
        print(f"   Password is ==> '{pswd}'")
"""


