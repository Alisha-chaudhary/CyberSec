"""
regex_flagged_ip_checker.py
Extracts IPs from log text and checks them against a list of flagged (suspicious) IP addresses.
"""

import re

# Example flagged list (replace with your own threat intel source)
FLAGGED_IPS = [
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144",
]

def extract_ips(text):
    """Extracts IPv4 patterns from text."""
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    return re.findall(pattern, text)

def check_flagged_ips(text):
    """
    Returns a list of tuples:
    (ip, "FLAGGED") or (ip, "OK")
    """
    extracted = extract_ips(text)
    results = []

    for ip in extracted:
        if ip in FLAGGED_IPS:
            results.append((ip, "FLAGGED"))
        else:
            results.append((ip, "OK"))

    return results


# Example execution
if __name__ == "__main__":
    log_data = """
    Unauthorized access attempt detected from 192.168.96.200.
    Normal activity from 10.0.0.5.
    Additional failed login from 192.168.168.144.
    """
    output = check_flagged_ips(log_data)

    print("IP Analysis Results:")
    for ip, status in output:
        print(f"  {ip}: {status}")
