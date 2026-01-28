import hashlib
import os

def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""): # Read file in 4KB chunks to ensure memory efficiency
                sha256_hash.update(byte_block) # Update the hash with the chunk
        return sha256_hash.hexdigest() # Return the final hexadecimal hash
    except FileNotFoundError:
        return None
    
def monitor_file_integrity(filepath): # Monitor and report file integrity
    vault_path = "systems/integrity_vault.txt" # Path to store file hashes
    found = False

    current_hash = calculate_hash(filepath) # Calculate current hash of the file
    if current_hash is None:
        print(f" [-] Error: File '{filepath}' not found.") # Handle file not found error
        return
    
    if os.path.exists(vault_path): # Check if vault file exists
         with open(vault_path, "r" ) as vault_file: # Open vault file for reading
            for line in vault_file: # Read each line in the vault file
                stored_filepath, stored_hash = line.strip().split(',') # Split line into filepath and hash

                if stored_filepath == filepath:  # Check if the file is already monitored            
                    found = True
                    if current_hash != stored_hash: # Compare current hash with stored hash
                            print(f" [!] ALERT: File has been modified! ") # Alert if file integrity is compromised
                            print(f" [+] Old hash: {stored_hash}") # Display old hash
                            print(f" [+ New hash: {current_hash}]") # Display new hash
                    else:
                            print(f" [*] File integrity verified. Hash: {stored_hash}") # File is unmodified
                   
                    print(f"[*] File already monitored. Stored hash: {stored_hash}") # Inform if file is already monitored            

    print(f"\n[*] Monitoring file integrity for: {filepath}")
    

    with open(vault_path, "a") as vault_file:
        vault_file.write(f"{filepath},{current_hash}\n")
    
    print(f" [+] New baseline created and stored.")
    print(f" [+] Current hash: {current_hash}")

if __name__ == "__main__":
    test_filepath = input("Enter the file path to monitor: ")
    monitor_file_integrity(test_filepath)