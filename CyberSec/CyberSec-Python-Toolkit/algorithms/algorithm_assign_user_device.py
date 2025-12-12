"""
algorithm_assign_user_device.py
Assigns users to device IDs using a simple algorithm.
Used in asset management and inventory tracking.
"""

def assign_devices(users, devices):
    """
    Assigns each user a device from the devices list.
    Assumes lists are aligned in order.

    Returns a dictionary: {user: device}
    """
    assignments = {}

    for i in range(len(users)):
        assignments[users[i]] = devices[i]

    return assignments


# Example execution
if __name__ == "__main__":
    users = ["elarson", "bmoreno", "sgilmore"]
    devices = ["r15router01", "r15switch07", "r15laptop22"]

    result = assign_devices(users, devices)

    print("User → Device Assignments:")
    for user, device in result.items():
        print(f"  {user}: {device}")
