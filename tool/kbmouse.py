import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# Mouse
MOUSE_LEFTDOWN = 0x0002     # left button down 
MOUSE_LEFTUP = 0x0004       # left button up 
MOUSE_RIGHTDOWN = 0x0008    # right button down 
MOUSE_RIGHTUP = 0x0010      # right button up 
MOUSE_MIDDLEDOWN = 0x0020   # middle button down 
MOUSE_MIDDLEUP = 0x0040     # middle button up 

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12



'''
# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]
         
'''
         
#####   
wintypes.ULONG_PTR = wintypes.WPARAM          
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,ki=KEYBDINPUT(wVk=hexKeyCode,dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


# Mouse Functions
def MoveMouse(x, y):
    ctypes.windll.user32.SetCursorPos(x,y)
    
def MouseMoveTo(x, y):
    extra = 0#ctypes.c_ulong(0)
    ii_ = INPUT._INPUT()
    #x = 1 + int(x * 65536/1920)#1920 width of your desktop
    #y = 1 + int(y * 65536/1080)#1080 height of your desktop
    #x = int(x*(65536/ctypes.windll.user32.GetSystemMetrics(0))+1)
    #y = int(y*(65536/ctypes.windll.user32.GetSystemMetrics(1))+1)
    
    #ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))
    ii_.mi = MOUSEINPUT(dx=x, dy=y, mouseData=0, dwFlags=0x0001, time=0, dwExtraInfo=wintypes.ULONG_PTR(extra))

    command = INPUT(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

def MouseLeftClick(delay=0):
    ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN,0,0,0,0)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)

def MouseRightClick(delay=0):
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTDOWN ,0,0,0,0)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTUP,0,0,0,0)

def MouseMiddleClick(delay=0):
    ctypes.windll.user32.mouse_event(MOUSE_MIDDLEDOWN ,0,0,0,0)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(MOUSE_MIDDLEDOWN ,0,0,0,0)
        
def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    PressKey(VK_TAB) 
    ReleaseKey(VK_TAB)
    time.sleep(2)
    ReleaseKey(VK_MENU) # Alt~

def Typein():
    text = input("enter to type: ")

    time.sleep(3)
    for t in text:
        acode = ord(t)
        #print(f"printing {t} = {acode} = {hcode} {vcode}")       
        PressKey(acode)
        
        ReleaseKey(acode)


def MultiClick(num):
    time.sleep(5)
    for i in range(num):
        MouseLeftClick(0)

def MouseKeepAlive():
    while(True):
        for i in range(100):
            MoveMouse(800+i,500)
            time.sleep(0.01)
        
        for i in range(100):
            MoveMouse(900-i,500)
            time.sleep(0.01)
        

if __name__ == "__main__":
    #time.sleep(5)
    #AltTab()
    # mouse = Mouse()
    #MouseKeepAlive()
    #MultiClick(500)
    Typein()
    


