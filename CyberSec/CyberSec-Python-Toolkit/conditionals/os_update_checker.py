"""
os_update_checker.py
Checks whether the operating system version is up-to-date.
"""

def check_os_version(version):
    """
    Returns whether the OS is updated based on known version requirements.
    OS2 = up-to-date
    OS1 / OS3 = update required
    Any other value = unknown or unsupported OS
    """
    if version == "OS 2":
        return "OS Status: Up-to-date — No action needed."
    elif version in ["OS 1", "OS 3"]:
        return "OS Status: Update required — Please install the latest patches."
    else:
        return "OS Status: Unsupported OS — Manual review recommended."


# Sample execution
if __name__ == "__main__":
    user_input = input("Enter OS version (OS 1, OS 2, OS 3): ")
    print(check_os_version(user_input))
