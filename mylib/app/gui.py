import ctypes
import ctypes.wintypes
from tkinter import Tk, simpledialog


# Define necessary constants
OFN_EXPLORER = 0x00080000
OFN_FILEMUSTEXIST = 0x00001000
OFN_HIDEREADONLY = 0x00000004

# Define necessary structures
class OPENFILENAME(ctypes.Structure):
    _fields_ = [("lStructSize", ctypes.wintypes.DWORD),
                ("hwndOwner", ctypes.wintypes.HWND),
                ("hInstance", ctypes.wintypes.HINSTANCE),
                ("lpstrFilter", ctypes.wintypes.LPCWSTR),
                ("lpstrCustomFilter", ctypes.wintypes.LPWSTR),
                ("nMaxCustFilter", ctypes.wintypes.DWORD),
                ("nFilterIndex", ctypes.wintypes.DWORD),
                ("lpstrFile", ctypes.wintypes.LPWSTR),
                ("nMaxFile", ctypes.wintypes.DWORD),
                ("lpstrFileTitle", ctypes.wintypes.LPWSTR),
                ("nMaxFileTitle", ctypes.wintypes.DWORD),
                ("lpstrInitialDir", ctypes.wintypes.LPCWSTR),
                ("lpstrTitle", ctypes.wintypes.LPCWSTR),
                ("Flags", ctypes.wintypes.DWORD),
                ("nFileOffset", ctypes.wintypes.WORD),
                ("nFileExtension", ctypes.wintypes.WORD),
                ("lpstrDefExt", ctypes.wintypes.LPCWSTR),
                ("lCustData", ctypes.wintypes.LPARAM),
                ("lpfnHook", ctypes.wintypes.LPVOID),
                ("lpTemplateName", ctypes.wintypes.LPCWSTR),
                ("pvReserved", ctypes.wintypes.LPVOID),
                ("dwReserved", ctypes.wintypes.DWORD),
                ("FlagsEx", ctypes.wintypes.DWORD)]


def OpenFile():
    # Define necessary functions
    GetOpenFileName = ctypes.windll.comdlg32.GetOpenFileNameW
    GetOpenFileName.argtypes = [ctypes.POINTER(OPENFILENAME)]
    GetOpenFileName.restype = ctypes.wintypes.BOOL

    # Create an instance of OPENFILENAME
    ofn = OPENFILENAME()
    ofn.lStructSize = ctypes.sizeof(OPENFILENAME)
    buffer = ctypes.create_unicode_buffer(260)
    ofn.lpstrFile = ctypes.cast(ctypes.pointer(buffer), ctypes.c_wchar_p)
    ofn.nMaxFile = 260
    ofn.Flags = OFN_EXPLORER | OFN_FILEMUSTEXIST | OFN_HIDEREADONLY

    # Display the file open dialog
    if GetOpenFileName(ctypes.byref(ofn)):
        return(buffer.value)


def MsgBox(title,text):
    # Define the MessageBoxW function from user32.dll
    MessageBox = ctypes.windll.user32.MessageBoxW

    # Define the text and title of the message box
    #text = "Hello, World!"
    #title = "My Message Box"

    # Call the MessageBoxW function
    result = MessageBox(0, text, title, 1)

    # Print the result
    return(result)

def InputBox(title,prompt):
    # we don't want a full GUI, so keep the root window from appearing
    root = Tk()
    root.withdraw()

    # show an input box
    user_input = simpledialog.askstring(title=title, prompt=prompt)

    # print the user's input
    print(user_input)
