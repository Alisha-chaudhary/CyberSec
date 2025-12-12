"""
device_id_parser.py
Parses device IDs into meaningful components using slicing and indexing.

Example device ID formats from certificate labs:
- r15-network-device
- r15router
- r15laptop001
"""

def parse_device_id(device_id):
    """
    Extracts the prefix, numeric section, and remaining string.
    Example: 'r15router' → prefix='r', code='15', label='router'
    """
    device_id = device_id.strip()

    prefix = device_id[0]               # first character
    numeric_code = device_id[1:3]       # the next two digits
    label = device_id[3:]               # the remaining string

    return {
        "prefix": prefix,
        "numeric_code": numeric_code,
        "label": label
    }


# Example execution
if __name__ == "__main__":
    sample = input("Enter a device ID: ")
    result = parse_device_id(sample)

    print("Parsed Device ID:")
    for key, value in result.items():
        print(f"  {key}: {value}")
