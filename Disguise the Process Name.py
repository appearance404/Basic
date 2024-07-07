# You can rename the script process to something less suspicious:
import ctypes
import os

def disguise_process():
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    pid = os.getpid()
    kernel32.SetConsoleTitleW(f"System Process {pid}")

disguise_process()
