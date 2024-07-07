import platform

def check_os_version():
    version = platform.version()
    if "10" in version:
        return "Windows 10"
    elif "6.3" in version:
        return "Windows 8.1"
    elif "6.2" in version:
        return "Windows 8"
    elif "6.1" in version:
        return "Windows 7"
    else:
        return "Unsupported OS"

os_version = check_os_version()
if os_version == "Unsupported OS":
    sys.exit("Unsupported OS")
