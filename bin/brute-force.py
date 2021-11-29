import itertools
import string
import msvcrt
from random import *
import time
import random

""" BRUTE FORCE """

def RandomGuess(password,letters = string.ascii_lowercase + "_" + string.digits):
    """randomly gussing"""
    while (True):
        try:
            guess = ""
            perm = ""
            for letter in range(len(password)):
                guessletter = letters[randint(0, len(letters))]
                guess = str(guessletter) + str(guess)
                perm = itertools.permutations(guess)
                
                for p in perm:
                    guess = "".join(p)
                    if(len(guess) == len(password)):
                        yield  guess
        except Exception as e:
            continue
            
                


def BruteForce(real,chars = string.ascii_lowercase + "_" + string.digits):
    """sequential guess"""
    for password_length in range(len(real),16):
        for guessWord in itertools.product(chars, repeat=password_length):
            guessWord = ''.join(guessWord)

            if(msvcrt.kbhit()) or len(guessWord) > len(real):
                break 

            if len(guessWord) == len(real):
                yield guessWord
                


def PermBruteForce(real,chars = string.ascii_lowercase + "_" + string.digits):
    """sequence with permutation"""
    for password_length in range(len(real),16):
        for guessWord in itertools.product(chars, repeat=password_length):
            guessWord = ''.join(guessWord)

            if(msvcrt.kbhit()) or len(guessWord) > len(real):
                break

            if len(guessWord) == len(real):
                perm = itertools.permutations(guessWord)
                
                for p in perm:
                    guessWord = "".join(p)
                    yield  guessWord


def RandomChoice(numof,chars = string.ascii_lowercase + "_" + string.digits):
    """ Random Permutation"""
    paswd = random.choices(chars,k=numof)
    res = ''.join(paswd)
    yield res



# Tests

stxt = "mca"

then = time.time()
attempt=0
for g in RandomGuess(stxt):
    attempt += 1
    print(g,end="\r")
    if(g == stxt):
        print(f" ==>",g,end="\n")
        break

now = time.time() - then
print(f" RandomGuess :: testing '{stxt}'")
print(f"[RandomGuess] :: {now} seconds elapsed")
print(f"[RandomGuess] :: {attempt} attempts",end="\n")

then = time.time()
attempt=0
for g in BruteForce(stxt):
    attempt += 1
    print(g,end="\r")
    if(g == stxt):
        print(f" ==>",g,end="\n")
        break

now = time.time() - then
print(f" BruteForce :: testing '{stxt}'")
print(f"[BruteForce] :: {now} seconds elapsed")
print(f"[BruteForce] :: {attempt} attempts",end="\n")

then = time.time()

attempt=0
for g in PermBruteForce(stxt):
    attempt += 1
    print(g,end="\r")
    if(g == stxt):
        print(f" ==>",g,end="\n")
        break

now = time.time() - then
print(f"PermBruteForce :: testing '{stxt}'")
print(f"[PermBruteForce] :: {now} seconds elapsed")
print(f"[PermBruteForce] :: {attempt} attempts")


attempt=0
g=""
while(g != stxt):
    g = next(RandomChoice(len(stxt)))
    attempt += 1
    
print(f" ==>",g,end="\n")


now = time.time() - then
print(f"RandomChoice :: testing '{stxt}'")
print(f"[RandomChoice] :: {now} seconds elapsed")
print(f"[RandomChoice] :: {attempt} attempts")
