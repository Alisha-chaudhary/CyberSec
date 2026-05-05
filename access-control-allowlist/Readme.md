# Allow List Update Script

## Overview
This project contains a Python script designed to help cybersecurity analysts manage access control by updating an allow list of IP addresses. The script reads a text file containing IPs that are permitted to access restricted content and removes any IPs that no longer have authorization.

This aligns with real-world cybersecurity workflows where analysts must routinely maintain, update, and validate access control lists to protect sensitive systems.

---

## Features
- Reads an existing list of allowed IP addresses from a text file  
- Removes IPs specified in a separate “remove list”  
- Updates the original file with the cleaned list  
- Simple, readable, and professional code suitable for beginner analysts and engineers alike  

---

## Use Case
You're working as a security analyst responsible for managing who can access restricted content. Over time, certain IP addresses should no longer have permission. This script automates the removal process so the allow list stays accurate and secure.

---

## How It Works
1. The script opens and reads the allow list file (`allow_list.txt`).
2. It splits the contents into a list of IP addresses.
3. It filters out any IPs that appear in the `remove_list`.
4. It writes the updated list back into the same file.

---

## Files Included
- **update_allow_list.py** – Main Python script  
- **allow_list.txt** – Sample file containing allowed IPs (you can replace this with your own)  

---

## How to Run
1. Place `update_allow_list.py` and `allow_list.txt` in the same folder.
2. Update the IPs inside your `remove_list` in the function call.
3. Run the script:

```bash
python3 update_allow_list.py
