# Script Name: update_allow_list.py
# Purpose: Reads a file of allowed IP addresses, removes IPs that should no longer
#          have access to restricted content, and updates the file with the cleaned list.
# Context: Designed for a cybersecurity workflow involving access control maintenance,
#          where outdated or unauthorized IP addresses must be automatically removed.
# Author: Alisha Chaudhary


# define and function called update_file
def update_file(import_file, remove_list):
    """
    Reads a file of IP addresses, removes any IPs in remove_list,
    and writes the updated list back to the same file.
    """

    # Read the file and split the IPs into a list
    with open(import_file, "r") as file:
        ip_addresses = file.read().split()

    # Keep only the IPs that are NOT in remove_list
    cleaned_ips = [ip for ip in ip_addresses if ip not in remove_list]

    # Write the updated list back into the file
    with open(import_file, "w") as file:
        file.write(" ".join(cleaned_ips))


# Example usage
update_file("allow_list.txt", ["192.168.1.1", "10.0.0.5"])

# Check the updated file
with open("allow_list.txt", "r") as file:
    print(file.read())
