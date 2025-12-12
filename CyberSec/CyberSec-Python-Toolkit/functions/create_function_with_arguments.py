"""
Practice using function arguments, return values, and cybersecurity-themed logic.
"""

def greet_user(username):
    return f"Welcome, {username}. Security dashboard loading..."

def failed_attempts(count):
    return f"Failed login attempts recorded: {count}"

def calculate_risk(score):
    if score >= 7:
        return "High risk – immediate investigation required."
    elif score >= 4:
        return "Medium risk – continue monitoring."
    else:
        return "Low risk – no action needed."

# Example calls
print(greet_user("analyst01"))
print(failed_attempts(3))
print(calculate_risk(8))
