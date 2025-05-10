import hashlib
import os
import json

# File to store known hashes
HASH_DB = 'hash_store.json'

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of the given file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

def load_hashes():
    """Load saved hashes from JSON file."""
    if os.path.exists(HASH_DB):
        with open(HASH_DB, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    """Save current file hashes to JSON file."""
    with open(HASH_DB, 'w') as f:
        json.dump(hashes, f, indent=4)

def monitor_files(file_list):
    """Compare current file hashes to saved ones."""
    old_hashes = load_hashes()
    current_hashes = {}

    for file_path in file_list:
        hash_value = calculate_hash(file_path)
        if hash_value is None:
            continue

        current_hashes[file_path] = hash_value
        old_hash = old_hashes.get(file_path)

        if old_hash is None:
            print(f"[NEW] {file_path}: Tracking new file.")
        elif old_hash != hash_value:
            print(f"[ALERT] {file_path}: File has been MODIFIED!")
        else:
            print(f"[OK] {file_path}: No changes detected.")

    save_hashes(current_hashes)

if __name__ == "__main__":
    # 🔧 List files you want to track here:
    files_to_check = [
        "example1.txt",
        "example2.txt",
        "your_new_file.txt",
        
    
    ]

    monitor_files(files_to_check)
