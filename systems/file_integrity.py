import hashlib
import os

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""): # Read file in 4KB chunks to ensure memory efficiency
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    
def monitor_file_integrity(filepath):
    vault_path = "systems/integrity_vault.txt"
    found = False

    current_hash = calculate_hash(filepath)
    if current_hash is None:
        print(f" [-] Error: File '{filepath}' not found.")
        return
    
    if os.path.exists(vault_path):
         with open(vault_path, "r" ) as vault_file:
            for line in vault_file:
                stored_filepath, stored_hash = line.strip().split(',')

                if stored_filepath == filepath:                  
                    found = True
                    if current_hash != stored_hash:
                            print(f" [!] ALERT: File has been modified! ")
                            print(f" [+] Old hash: {stored_hash}")
                            print(f" [+ New hash: {current_hash}]")
                    else:
                            print(f" [*] File integrity verified. Hash: {stored_hash}")
                    return

                    print(f"[*] File already monitored. Stored hash: {stored_hash}")
                    return

    print(f"\n[*] Monitoring file integrity for: {filepath}")
    

    with open(vault_path, "a") as vault_file:
        vault_file.write(f"{filepath},{current_hash}\n")
    
    print(f" [+] New baseline created and stored.")
    print(f" [+] Current hash: {current_hash}")

if __name__ == "__main__":
    test_filepath = input("Enter the file path to monitor: ")
    monitor_file_integrity(test_filepath)