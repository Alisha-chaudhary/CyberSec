"""
algorithm_update_allowlist.py
Updates an allow list by adding newly approved IP addresses.
Demonstrates list manipulation and access control logic.
"""

def update_allowlist(allow_list, new_ips):
    """
    Extends the allow_list with new IP addresses.
    Returns the updated list.
    """
    allow_list.extend(new_ips)
    return allow_list


# Example execution
if __name__ == "__main__":
    allow_list = ["10.0.0.5", "192.168.1.10"]
    new_entries = ["172.16.0.2", "192.168.99.14"]

    updated = update_allowlist(allow_list, new_entries)

    print("Updated Allow List:")
    for ip in updated:
        print("  ", ip)
