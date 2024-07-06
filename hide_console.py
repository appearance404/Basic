import subprocess

def hide_console():
    subprocess.Popen('pythonw.exe ' + __file__, creationflags=subprocess.CREATE_NO_WINDOW)
