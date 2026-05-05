"""
login_analysis_function.py
Analyzes login attempts to detect suspicious activity.
"""

def analyze_logins(log_list):
    """
    Returns the count of suspicious logins.
    A suspicious login is defined as:
    - containing the word 'FAILED'
    """
    suspicious_count = 0

    for item in log_list:
        if "FAILED" in item.upper():
            suspicious_count += 1

    return suspicious_count

# Example usage
logins = [
    "User1 SUCCESS",
    "User2 FAILED",
    "User3 SUCCESS",
    "User4 FAILED",
    "User5 FAILED"
]

print("Suspicious login attempts:", analyze_logins(logins))
