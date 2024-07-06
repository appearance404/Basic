import subprocess

def hide_console():
    subprocess.Popen('pythonw.exe ' + __file__, creationflags=subprocess.CREATE_NO_WINDOW)


import os
import sys
import subprocess

def hide_console():
    # Check if the script is already running with pythonw.exe to avoid recursion
    if sys.executable.endswith('pythonw.exe'):
        return

    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)
    
    # Run the script with pythonw.exe to hide the console
    subprocess.Popen(['pythonw.exe', script_path], creationflags=subprocess.CREATE_NO_WINDOW)

# Call the function to hide the console
hide_console()
