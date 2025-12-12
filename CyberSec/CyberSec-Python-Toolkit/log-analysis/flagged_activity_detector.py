"""
flagged_activity_detector.py
Detects potentially malicious activity by comparing extracted IPs
from logs against a known list of flagged IP addresses.
"""

import re

FLAGGED_IPS = [
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144",
]

def extract_ips(text):
    """Extracts IPv4-like patterns from log text."""
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    return re.findall(pattern, text)

def detect_flagged_ips(filename):
    """
    Reads a log file and identifies IPs that match the flagged list.
    Returns a list of (ip, status) tuples.
    """
    with open(filename, "r") as file:
        content = file.read()

    ips = extract_ips(content)
    results = []

    for ip in ips:
        if ip in FLAGGED_IPS:
            results.append((ip, "FLAGGED"))
        else:
            results.append((ip, "OK"))

    return results


# Example execution
if __name__ == "__main__":
    filepath = "sample_files/login.txt"
    print(f"Analyzing log file: {filepath}\n")

    results = detect_flagged_ips(filepath)

    print("Flagged Activity Report:")
    for ip, status in results:
        print(f"  {ip}: {status}")
