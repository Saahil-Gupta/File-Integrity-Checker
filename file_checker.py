import hashlib
import os
import time
from datetime import datetime

# Set the file path you want to keep a close eye on
file_path = "test_file.txt"

# Where we'll save the file's hash for comparison later
hash_file = "file_hash.txt"

# How often to check for changes (in seconds). Lower the number, higher the computation usage
interval = 100

def calculate_hash(file_path):
    """Generate a SHA-256 hash of the file to track its content."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks (saves memory if the file is huge)
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] !!! The file '{file_path}' is missing.")
        return None

def save_hash(hash_value):
    """Store the hash in a file for future comparisons."""
    with open(hash_file, "w") as f:
        f.write(hash_value)

def load_hash():
    """Grab the saved hash from the file."""
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            return f.read()
    return None

def monitor_file():
    """Keep checking the file for any changes."""
    print(f"Keeping a close eye on '{file_path}' every {interval} seconds.....")
    original_hash = calculate_hash(file_path)

    # If the hash file doesn't exist, let's make one with the current hash
    if load_hash() is None:
        save_hash(original_hash)
        print("[INFO] Saved the initial hash.")

    while True:
        current_hash = calculate_hash(file_path)
        saved_hash = load_hash()

        # If the hashes don't match, something changed!
        if current_hash != saved_hash:
            print(f"[ALERT] !!!! The file was changed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"[INFO] Previous Hash: {saved_hash}")
            print(f"[INFO] New Hash: {current_hash}")
            print(f"[INFO] Change Detected: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Update the saved hash so we don't keep getting alerts
            save_hash(current_hash)
        else:
            print(f"[INFO] All good! No changes detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Take a breather before checking again
        time.sleep(interval)

if __name__ == "__main__":
    monitor_file()
