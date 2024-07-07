import ctypes
import os
import sys
import platform
import subprocess

def is_admin():
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        return os.geteuid() == 0
    else:
        raise Exception("Unsupported platform")

def run_as_admin():
    if platform.system() == "Windows":
        # Re-run the script with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit()
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        # Re-run the script with sudo
        print("Script requires elevated privileges, attempting to relaunch with sudo...")
        subprocess.check_call(['sudo', sys.executable] + sys.argv)
        sys.exit()
    else:
        raise Exception("Unsupported platform")

if not is_admin():
    run_as_admin()

# Your main script logic here
print("Running with admin privileges!")
