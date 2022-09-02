import msvcrt
import time


while(True):
    if(msvcrt.kbhit() and msvcrt.getwch() == "p"):
        print('Pause')
    if(msvcrt.kbhit() and msvcrt.getwch() == "x"):
        print("Exit")
        break
    print(time.time())
        
