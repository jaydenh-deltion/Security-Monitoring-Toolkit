import hashlib
import os

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    
def monitor_file_integrity(filepath):
    print(f"\n[*] Monitoring file integrity for: {filepath}\n")
    current_hash = calculate_hash(filepath)

    if current_hash is None:
        print(f" [-] Error: File '{filepath}'not found.")
        return
    
    print(f" [+] Current hash: {current_hash}")
    print("\n Tip: Copy this hash. If you change the file and run this again, you will see it changes! ")

if __name__ == "__main__":
    test_filepath = input("Enter the file path to monitor: ")
    monitor_file_integrity(test_filepath)