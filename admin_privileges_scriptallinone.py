import ctypes
import os
import sys
import platform
import subprocess

def ensure_admin_privileges():
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

    if not is_admin():
        if platform.system() == "Windows":
            # Re-run the script with admin rights on Windows
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
            sys.exit()
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            # Re-run the script with sudo on macOS (Darwin) and Linux
            print("Script requires elevated privileges, attempting to relaunch with sudo...")
            subprocess.check_call(['sudo', sys.executable] + sys.argv)
            sys.exit()
        else:
            raise Exception("Unsupported platform")

ensure_admin_privileges()

# Your main script logic here
print("Running with admin privileges!")
