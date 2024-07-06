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

# Your main script code goes here
print("The console is hidden, and the script is running.")
