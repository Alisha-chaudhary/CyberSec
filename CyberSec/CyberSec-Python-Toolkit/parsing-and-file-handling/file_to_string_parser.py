"""
file_to_string_parser.py
Reads an entire file as a single string.
Used commonly before applying regex for security log analysis.
"""

def file_to_string(filename):
    """
    Returns the full contents of a file as one continuous string.
    Useful when applying regex patterns across entire logs.
    """
    with open(filename, "r") as file:
        return file.read()


# Example execution
if __name__ == "__main__":
    filepath = "sample_files/example_devices.txt"
    content = file_to_string(filepath)

    print("Raw file content:\n")
    print(content)
