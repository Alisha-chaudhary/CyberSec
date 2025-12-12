"""
login_textfile_to_list.py
Reads login attempts from a text file and converts them into a list.
Useful for feeding into analysis functions (e.g., suspicious login detection).
"""

def load_login_attempts(filename):
    """
    Loads login attempts from a file.
    Each line is treated as a separate login event.
    """
    attempts = []
    with open(filename, "r") as file:
        for line in file:
            attempts.append(line.strip())
    return attempts


# Example usage
if __name__ == "__main__":
    filepath = "sample_files/login.txt"
    login_attempts = load_login_attempts(filepath)

    print("Login attempts:")
    for attempt in login_attempts:
        print(" >", attempt)
