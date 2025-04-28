import os
import shutil
import hashlib
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Function to get file hash
def get_file_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            hasher = hashlib.md5()
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, Exception) as e:
        print(f"Error reading file {file_path}: {e}")
        return None

# Function to handle duplicate file movement
def move_duplicate(file_path, duplicates_folder, file_name):
    base_name, ext = os.path.splitext(file_name)
    counter = 1
    duplicate_path = os.path.join(duplicates_folder, file_name)
    while os.path.exists(duplicate_path):
        duplicate_path = os.path.join(duplicates_folder, f"{base_name}_{counter}{ext}")
        counter += 1
    try:
        shutil.move(file_path, duplicate_path)
        print(f"Moved duplicate: {file_name}")
    except PermissionError:
        print(f"Permission denied: Unable to move {file_path}. Skipping...")

# Main function
def main():
    # Use tkinter to select folder
    Tk().withdraw()  # Hide the root tkinter window
    folder_dir = askdirectory(title="Select Folder to Check for Duplicates")
    if not folder_dir:
        print("No folder selected. Exiting...")
        return

    duplicates_folder = os.path.join(folder_dir, "Duplicate_Files")
    try:
        os.makedirs(duplicates_folder, exist_ok=True)
    except PermissionError:
        print(f"Permission denied: Unable to create folder in {folder_dir}. Exiting...")
        return

    file_hashes = {}
    duplicates_found = 0

    print("Starting duplicate file check...\n")
    for root, _, files in os.walk(folder_dir):
        # Skip system-protected directories
        if "Program Files" in root or "Windows" in root:
            print(f"Skipping system-protected directory: {root}")
            continue

        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                file_hash = get_file_hash(file_path)
                if file_hash:
                    if file_hash in file_hashes:
                        try:
                            move_duplicate(file_path, duplicates_folder, file_name)
                            duplicates_found += 1
                        except PermissionError:
                            print(f"Permission denied: Unable to move {file_path}. Skipping...")
                    else:
                        file_hashes[file_hash] = file_path

    # Summary
    print("\nDuplicate check complete!")
    if duplicates_found == 0:
        print("No duplicate files were found.")
    else:
        print(f"Total duplicates moved: {duplicates_found}")
        print(f"Duplicate files stored in: {duplicates_folder}")

if __name__ == "__main__":
    main()