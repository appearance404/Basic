import os
import sys
import subprocess

def hide_console():
    if os.name == 'nt':  # Windows
        # Check if the script is already running with pythonw.exe to avoid recursion
        if sys.executable.endswith('pythonw.exe'):
            return

        # Get the absolute path of the current script
        script_path = os.path.abspath(__file__)
        
        # Run the script with pythonw.exe to hide the console
        subprocess.Popen(['pythonw.exe', script_path], creationflags=subprocess.CREATE_NO_WINDOW)
        sys.exit()

    elif os.name == 'posix':  # macOS and Linux
        # Check if the script is already running as a daemon to avoid recursion
        if os.fork():
            sys.exit()
        os.setsid()
        if os.fork():
            sys.exit()
        sys.stdout.flush()
        sys.stderr.flush()
        with open('/dev/null', 'wb', 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
            os.dup2(f.fileno(), sys.stdout.fileno())
            os.dup2(f.fileno(), sys.stderr.fileno())

# Call the function to hide the console
hide_console()

'''
Explanation:
Windows:

The script checks if it is already running with pythonw.exe to avoid recursion.
It uses subprocess.Popen with CREATE_NO_WINDOW to run the script with pythonw.exe.
macOS and Linux:

The script uses os.fork to create a child process.
The child process becomes a session leader with os.setsid and forks again to detach from the terminal.
Standard input, output, and error are redirected to /dev/null.
Usage:
Save the script as a .py file.
Run the script using python.exe (Windows) or python (macOS/Linux) initially. The script will handle the rest to hide the console.
'''

# Your main script code goes here
print("The console is hidden, and the script is running.")
