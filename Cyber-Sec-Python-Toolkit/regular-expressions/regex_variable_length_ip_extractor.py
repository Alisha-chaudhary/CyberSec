"""
regex_variable_length_ip_extractor.py
Extracts IP addresses of ANY digit length before validation is applied.
Useful for pre-cleaning log files.
"""

import re

def extract_ip_variable(text):
    """
    Extracts IP-like patterns with no digit-length restriction.
    Example: 1.22.333.4444 (not validated)
    """
    pattern = r"\d+\.\d+\.\d+\.\d+"
    return re.findall(pattern, text)


# Example execution
if __name__ == "__main__":
    sample = "IPs found: 1.2.3.4, 22.155.3000.1, 9999.88.77.66"
    print("Extracted variable-length IPs:", extract_ip_variable(sample))
