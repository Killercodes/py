import os, sys


class Color:
        " color class"
        def DarkRed():
                return("\033[31m")

        def DarkGreen():
                return ("\033[32m")

        def DarkYellow(txt):
                return ("\033[33m " + txt)

        def DarkBlue(txt):
                return ("\033[34m " + txt)

        def DarkMagenta(txt):
                return ("\033[35m " + txt)

        def DarkCyan(txt):
                return ("\033[36m " + txt)

        def DarkWhite(txt):
                return ("\033[37m " + txt)

        def Underline(txt):
                return ("\033[4m " + txt)

        def RESET(txt):
                return (txt + " \033[0m")

        def Red():
                return("\33[91m")

        def Green():
                return("\33[92m")

        def Yellow():
                return("\33[93m")

        def Blue():
                return("\33[94m")

        def Magenta():
                return("\33[95m")

        def Cyan():
                return("\33[96m")

        def White():
                return("\33[97m")

        def HRed():
                return("\33[41m\33[97m")

        def HGreen():
                return("\33[97m\33[44m")

        def HBlue():
                return("\33[97m\33[44m")

#EOF          
