"""
algorithm_remove_ips.py
Removes specific IP addresses from a list.
Used for cleanup tasks such as removing retired devices or revoked access.
"""

def remove_ips(ip_list, to_remove):
    """
    Removes each IP in to_remove from ip_list (if present).
    Returns the cleaned list.
    """
    for ip in to_remove:
        if ip in ip_list:
            ip_list.remove(ip)
    return ip_list


# Example execution
if __name__ == "__main__":
    current_ips = ["10.0.0.1", "10.0.0.5", "192.168.1.3", "172.16.0.2"]
    revoked_ips = ["10.0.0.5", "172.16.0.2"]

    cleaned_list = remove_ips(current_ips, revoked_ips)

    print("Cleaned IP List:")
    for ip in cleaned_list:
        print("  ", ip)
