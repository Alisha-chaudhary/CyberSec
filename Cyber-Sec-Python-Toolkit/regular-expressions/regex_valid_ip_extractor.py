"""
Extracts VALID IPv4 addresses with proper octet length (0–255 not enforced here).
Pattern: 1–3 digits per octet.
"""

import re

def extract_valid_ips(text):
    """
    Returns a list of IPv4 addresses using a stricter pattern than basic extraction.
    Still does not validate numeric ranges, just digit ranges.
    """
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    return re.findall(pattern, text)


# Example execution
if __name__ == "__main__":
    log_data = "Failed attempt from 192.168.200.2, success from 10.0.0.1"
    print("Valid-format IPs:", extract_valid_ips(log_data))
