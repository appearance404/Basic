import os
import sys

def disguise_process():
    pid = os.getpid()
    title = f"System Process {pid}"

    if sys.platform.startswith('win'):
        # Windows
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        # Linux or macOS
        sys.stdout.write(f"\x1b]2;{title}\x07")
    else:
        raise NotImplementedError("Unsupported platform")

disguise_process()
