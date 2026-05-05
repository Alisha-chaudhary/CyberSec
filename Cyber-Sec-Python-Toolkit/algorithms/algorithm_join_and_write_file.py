"""
algorithm_join_and_write_file.py
Joins a list of IP addresses and writes them to a new allow_list.txt file.
Used to finalize configuration files or update firewall rules.
"""

def write_allowlist_to_file(ip_list, filename):
    """
    Joins IP addresses with newline characters and writes to filename.
    """
    with open(filename, "w") as file:
        file.write("\n".join(ip_list))


# Example execution
if __name__ == "__main__":
    final_allowlist = [
        "10.0.0.1",
        "192.168.1.10",
        "172.16.0.2"
    ]

    output_path = "sample_files/allow_list.txt"
    write_allowlist_to_file(final_allowlist, output_path)

    print(f"Allow list successfully written to {output_path}")
