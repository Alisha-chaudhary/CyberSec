"""
employee_id_standardizer.py
Standardizes employee ID numbers into a consistent format for system logging.
Example:
Input: 4186 → Output: "E4186"
"""

def standardize_employee_id(emp_id):
    """
    Takes an integer or string employee ID and returns it in the format 'E####'.
    """
    emp_str = str(emp_id).strip()

    if not emp_str.isdigit():
        return "Invalid ID — must contain only digits."

    return f"E{emp_str}"


# Example execution
if __name__ == "__main__":
    user_input = input("Enter employee ID: ")
    print("Standardized ID:", standardize_employee_id(user_input))
