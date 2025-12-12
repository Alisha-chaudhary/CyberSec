"""
log_file_viewer.py
Basic log viewer that prints log file contents with line numbers.
Useful for manual inspection during initial incident triage.
"""

def view_log_file(filename):
    """
    Reads a log file and prints each line with a line number.
    """
    with open(filename, "r") as file:
        for number, line in enumerate(file, start=1):
            print(f"{number:03}: {line.strip()}")


# Example execution
if __name__ == "__main__":
    filepath = "sample_files/login.txt"
    print(f"Viewing log file: {filepath}\n")
    view_log_file(filepath)
