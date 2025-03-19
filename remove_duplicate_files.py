import os
import shutil
import hashlib

# Function to get file hash
def get_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None

# Folder path where files are stored
folder_dir = r"C:\Users\HP\Downloads"
duplicates_folder = os.path.join(folder_dir, "Duplicate_Files")
os.makedirs(duplicates_folder, exist_ok=True)

# Dictionary to track file hashes
file_hashes = {}
duplicates_found = 0

# Check for duplicates
for file_name in os.listdir(folder_dir):
    file_path = os.path.join(folder_dir, file_name)
    
    if os.path.isfile(file_path):  
        file_hash = get_file_hash(file_path)

        if file_hash and file_hash in file_hashes:
            shutil.move(file_path, os.path.join(duplicates_folder, file_name))  # Move duplicate
            print(f"Moved duplicate: {file_name}")
            duplicates_found += 1
        else:
            file_hashes[file_hash] = file_path  # Store unique file hash

# Summary
print("\nDuplicate check complete!")
print(f"Total duplicates moved: {duplicates_found}")
print(f"Duplicate files stored in: {duplicates_folder}")
