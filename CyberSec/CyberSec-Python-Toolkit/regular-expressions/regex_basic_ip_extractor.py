"""
regex_basic_ip_extractor.py
Extracts IP-like patterns using a simple regex.
Note: This version does NOT validate IP ranges (0–255).
"""

import re

def extract_ip_basic(text):
    """
    Returns all sequences that look like IPv4 addresses.
    Allows any sequence of 1–3 digits between dots.
    Example matches: 192.168.0.1, 300.455.89.999 (not validated)
    """
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    return re.findall(pattern, text)


# Example execution
if __name__ == "__main__":
    sample_log = "User connected from 192.168.1.10 and backup IP 255.300.22.5"
    print("Extracted IPs:", extract_ip_basic(sample_log))
