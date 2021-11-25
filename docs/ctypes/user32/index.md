# Win32 API - User32 example

```py
import ctypes
user32 = ctypes.windll.user32

# get screen resolution of primary monitor
res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
# res is (2293, 960) for 3440x1440 display at 150% scaling
user32.SetProcessDPIAware()
res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
# res is now (3440, 1440) for 3440x1440 display at 150% scaling

# get handle for Notepad window
# non-zero value for handle should mean it found a window that matches
handle = user32.FindWindowW(u'Notepad', None)
# or
handle = user32.FindWindowW(None, u'Untitled - Notepad')

# meaning of 2nd parameter defined here
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms633548(v=vs.85).aspx
# minimize window using handle
user32.ShowWindow(handle, 6)
# maximize window using handle
user32.ShowWindow(handle, 9)

# move window using handle
# MoveWindow(handle, x, y, height, width, repaint(bool))
user32.MoveWindow(handle, 100, 100, 400, 400, True)

# Move cursor to x,y
user32.SetCursorPos(500,500)
```
