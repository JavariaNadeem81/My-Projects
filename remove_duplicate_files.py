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
        print(f"Permission denied: {file_path}. Skipping...")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Get folder path from user
folder_dir = input("Enter the folder path to check for duplicates: ").strip()
if not os.path.exists(folder_dir):
    print("The specified folder does not exist. Exiting...")
    exit()

duplicates_folder = os.path.join(folder_dir, "Duplicate_Files")
os.makedirs(duplicates_folder, exist_ok=True)

# Dictionary to track file hashes
file_hashes = {}
duplicates_found = 0

# Check for duplicates
print("Starting duplicate file check...\n")
for root, _, files in os.walk(folder_dir):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)

            if file_hash and file_hash in file_hashes:
                try:
                    # Handle duplicate file name conflict
                    duplicate_path = os.path.join(duplicates_folder, file_name)
                    base_name, ext = os.path.splitext(file_name)
                    counter = 1
                    while os.path.exists(duplicate_path):
                        duplicate_path = os.path.join(duplicates_folder, f"{base_name}_{counter}{ext}")
                        counter += 1

                    shutil.move(file_path, duplicate_path)  # Move duplicate
                    print(f"Moved duplicate: {file_name}")
                    duplicates_found += 1
                except Exception as e:
                    print(f"Error moving file {file_name}: {e}")
            else:
                file_hashes[file_hash] = file_path  # Store unique file hash
        else:
            print(f"Skipping non-file item: {file_name}")

# Summary
print("\nDuplicate check complete!")
print(f"Total duplicates moved: {duplicates_found}")
print(f"Duplicate files stored in: {duplicates_folder}")
print("This script works for all file types, including images, cache files, and more.")
