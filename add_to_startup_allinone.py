import os
import sys

def add_to_startup(file_path):
    if sys.platform.startswith('win'):
        import winreg as reg
        key = reg.HKEY_CURRENT_USER
        key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        
        open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(open_key, "MyApp", 0, reg.REG_SZ, file_path)
        reg.CloseKey(open_key)
    
    elif sys.platform == 'darwin':
        startup_file = os.path.expanduser('~/Library/LaunchAgents/com.myapp.startup.plist')
        plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.myapp.startup</string>
    <key>ProgramArguments</key>
    <array>
        <string>{file_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>'''
        with open(startup_file, 'w') as f:
            f.write(plist_content)
        os.system(f'launchctl load {startup_file}')
    
    elif sys.platform.startswith('linux'):
        autostart_dir = os.path.expanduser('~/.config/autostart/')
        if not os.path.exists(autostart_dir):
            os.makedirs(autostart_dir)
        startup_file = os.path.join(autostart_dir, 'myapp.desktop')
        desktop_entry = f'''[Desktop Entry]
Type=Application
Exec={file_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=MyApp
Comment=Start MyApp at login'''
        with open(startup_file, 'w') as f:
            f.write(desktop_entry)
    
    else:
        raise NotImplementedError(f"Unsupported platform: {sys.platform}")

# Example usage
add_to_startup(os.path.abspath(__file__))
