"""
url_parser_full.py
Parses URLs to extract protocol, domain, and file extension
using string methods such as index(), slicing, and split().
"""

def parse_url(url):
    """
    Extracts protocol, domain, and extension from a well-structured URL.
    Example:
    Input:  "https://example.com/security/report.html"
    Output: protocol='https', domain='example.com', extension='html'
    """
    url = url.strip()

    # Extract protocol
    protocol_end = url.index("://")
    protocol = url[:protocol_end]

    # Remove protocol for easier processing
    rest = url[protocol_end + 3:]

    # Extract domain
    first_slash = rest.index("/")
    domain = rest[:first_slash]

    # Extract file extension
    if "." in rest:
        extension = rest.split(".")[-1]
    else:
        extension = "No extension detected"

    return {
        "protocol": protocol,
        "domain": domain,
        "extension": extension
    }


# Example execution
if __name__ == "__main__":
    url_input = input("Enter a URL: ")
    result = parse_url(url_input)

    print("\nParsed URL Components:")
    for key, value in result.items():
        print(f"  {key}: {value}")
