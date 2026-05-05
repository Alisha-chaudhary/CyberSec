"""
ip_extraction_workflow.py
Complete workflow for extracting IP addresses from log files.
Uses regex to identify IPv4 patterns and returns a deduplicated list.
"""

import re

def read_file_as_string(filename):
    """Returns the entire contents of a file as a single string."""
    with open(filename, "r") as file:
        return file.read()

def extract_ips(text):
    """
    Extracts valid-format IPv4 addresses using regex.
    Does not enforce octet range validation.
    """
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    return re.findall(pattern, text)

def extract_unique_ips(filename):
    """
    Reads a log file, extracts all IPs, and returns a unique sorted list.
    """
    content = read_file_as_string(filename)
    ips = extract_ips(content)
    return sorted(set(ips))


# Example execution
if __name__ == "__main__":
    filepath = "sample_files/login.txt"
    print(f"Extracting IPs from: {filepath}\n")

    unique_ips = extract_unique_ips(filepath)
    print("Unique IPs found:")
    for ip in unique_ips:
        print("  ", ip)
