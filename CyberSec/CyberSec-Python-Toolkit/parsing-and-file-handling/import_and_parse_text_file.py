"""
import_and_parse_text_file.py
Reads a text file and prints each line after stripping whitespace.
Use-case: Initial log ingestion during security analysis.
"""

def read_file_lines(filename):
    """
    Reads all lines from a file and returns a cleaned list.
    Removes trailing newline characters and surrounding whitespace.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


# Example execution
if __name__ == "__main__":
    filepath = "sample_files/login.txt"
    lines = read_file_lines(filepath)

    print(f"Contents of {filepath}:")
    for line in lines:
        print(" -", line)
