# file_integrity_checker.py
# "COMPANY":CODTECH IT SOLUTIONS
# "NAME":MUDAVATH MALLESH NAYAK
# "INTERN ID":CT04DL263
# "DOMAIN":CYBER SECURITY AND ETHICAL HACKING
# "DURATION": 4 WEEKS
# "MENTOR":NEELA SANTOSH KUMAR
# The File Integrity Checker is a Python-based script designed to monitor and verify the integrity of files by using cryptographic hash values. Its primary function is to detect any unauthorized modifications, deletions, or additions to files by comparing their current SHA-256 hash values with previously stored hashes. The script uses standard Python libraries such as os for file system operations, hashlib for generating secure hashes, and json for storing and retrieving hash data from a file named hash_store.json. On the initial run, the script generates hashes for all target files and stores them in the JSON file. During subsequent runs, it recalculates the hashes and compares them to the stored values to detect changes. If a file is unmodified, it returns [OK]; if it is altered, [ALERT]; if newly added, [NEW]; and if missing, [ERROR]. This tool is useful for basic file security auditing, ensuring file consistency, and tracking changes in environments where file integrity is essential. Developed entirely in Python 3, the script requires no external dependencies, making it lightweight and easy to use.
# "OUTPUT":
![Image](https://github.com/user-attachments/assets/c00b46cf-98a1-4412-9838-98f067eb6500)
