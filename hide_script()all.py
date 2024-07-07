import shutil
import os
import platform

def hide_script():
    current_platform = platform.system()
    script_path = os.path.abspath(__file__)

    if current_platform == 'Windows':
        hidden_dir = os.path.join(os.getenv('APPDATA'), 'SystemCache')
        if not os.path.exists(hidden_dir):
            os.makedirs(hidden_dir)
        hidden_path = os.path.join(hidden_dir, os.path.basename(script_path))
        if script_path != hidden_path:
            shutil.copy2(script_path, hidden_path)
            os.system(f'attrib +h {hidden_path}')
            os.system(f'attrib +h {hidden_dir}')

    elif current_platform == 'Darwin':  # macOS
        hidden_dir = os.path.join(os.path.expanduser('~'), '.SystemCache')
        if not os.path.exists(hidden_dir):
            os.makedirs(hidden_dir)
        hidden_path = os.path.join(hidden_dir, os.path.basename(script_path))
        if script_path != hidden_path:
            shutil.copy2(script_path, hidden_path)
            os.rename(hidden_path, hidden_path + '.')  # Add a dot to the file name to hide it

    elif current_platform == 'Linux':
        hidden_dir = os.path.join(os.path.expanduser('~'), '.SystemCache')
        if not os.path.exists(hidden_dir):
            os.makedirs(hidden_dir)
        hidden_path = os.path.join(hidden_dir, os.path.basename(script_path))
        if script_path != hidden_path:
            shutil.copy2(script_path, hidden_path)
            os.rename(hidden_path, hidden_path + '.')  # Add a dot to the file name to hide it

    return hidden_path

script_path = hide_script()
print(f'Script moved to hidden path: {script_path}')
