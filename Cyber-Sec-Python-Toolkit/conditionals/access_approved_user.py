"""
access_approved_user.py
Checks if a user is authorized based on an approved user (allow) list.
"""

approved_users = ["elarson", "tshah", "bmoreno", "sgilmore", "eraab"]

def check_access(username):
    """
    Returns True if user is authorized, otherwise False.
    """
    return username in approved_users


# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")

    if check_access(username):
        print(f"Access granted: {username} is authorized.")
    else:
        print(f"Access denied: {username} is not on the approved list.")
