#demo colors

import sys

print ("\u001b[1m BOLD \u001b[0m\u001b[4m Underline \u001b[0m\u001b[7m")

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print (u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print ("\u001b[0m")

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print (u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print ("\u001b[0m")
    
#EOF
