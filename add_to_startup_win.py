import winreg as reg
import os

def add_to_startup(file_path):
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    
    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_key, "MyApp", 0, reg.REG_SZ, file_path)
    reg.CloseKey(open_key)

# Example usage
add_to_startup(os.path.abspath(__file__))
