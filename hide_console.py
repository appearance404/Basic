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

import subprocess
import sys

def hide_console():
    if sys.executable.endswith('pythonw.exe'):
        # The script is already running with pythonw.exe, no need to re-run
        return

    # Check if the script is being run interactively
    if not hasattr(sys, 'frozen'):
        try:
            subprocess.Popen([sys.executable.replace('python.exe', 'pythonw.exe'), __file__], 
                             creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as e:
            print(f"Failed to hide console: {e}")
        sys.exit()

# Call hide_console at the start of your script
hide_console()

# Your main script code here
print("This is a test script running without a console window.")

