"""
combined_access_logic.py
Combines user authorization and login timing rules using conditional logic.
"""

approved_users = ["elarson", "tshah", "bmoreno", "sgilmore", "eraab"]

def is_user_approved(username):
    return username in approved_users

def is_org_hours(hour):
    """
    org hours = 9 to 17 (9 AM to 5 PM)
    Adjust this based on policy from your certificate labs.
    """
    return 9 <= hour <= 17


# Combined logic
if __name__ == "__main__":
    username = input("Enter username: ")
    login_hour = int(input("Enter login hour (0–23): "))

    if is_user_approved(username) and is_org_hours(login_hour):
        print("Access granted: User approved AND login within organization hours.")
    elif not is_user_approved(username):
        print("Access denied: User not authorized.")
    else:
        print("Access denied: Login occurred outside organization hours.")
