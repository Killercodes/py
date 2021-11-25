# kbhit: Capturing keyboard event

## How to break the loop on pressing X
The following code will continut printing the time until you press `x` in your keyboard

```py
import msvcrt
import time


while(True):
    if(msvcrt.kbhit() and msvcrt.getwch() == "x"):
        print("Exit")
        break
    print(time.time())
```
