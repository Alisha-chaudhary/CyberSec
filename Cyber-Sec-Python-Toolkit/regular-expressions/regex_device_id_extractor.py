"""
regex_device_id_extractor.py
Extracts device IDs that follow a specific pattern using regular expressions.
Common use-case: Identify devices requiring updates (e.g., IDs starting with r15).
"""

import re

def extract_device_ids(text):
    """
    Extracts all device IDs starting with 'r15' followed by letters or digits.
    Example matches: r15router, r15laptop01, r15dev123
    """
    pattern = r"r15\w+"
    return re.findall(pattern, text)


# Example execution
if __name__ == "__main__":
    sample_text = """
    Connected devices:
    r15router, r15switch09, x22device, r15laptop001
    """
    devices = extract_device_ids(sample_text)
    print("Extracted device IDs:", devices)
