import os
import shutil

# Define the folder where files are stored
folder_dir = r"C:\Users\HP\Downloads"

# Define categories (extensions and their folders)
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Spreadsheets": [".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx"],
    "Archives": [".zip", ".rar"],
    "Installers": [".exe", ".msi"],
    "Virtual Machines": [".ova", ".vbox"],
    "Configs": [".dat", ".ini"],
    "OneNote": [".one"],
    "Configuration Files": [".config", ".ini"],
    "ISO Files": [".iso"],
    "Drawings": [".dwg", ".dxf"],
    "Encrypted Files": [".enc", ".dat"],
    "Executable Files": [".exe", ".msi"],
    "VirtualBox Files": [".vbox-extpack"],
     "CSV Files": {".csv"},
    "RIS Files": {".ris"}
}

# Create folders if they don’t exist
for category in file_types:
    category_path = os.path.join(folder_dir, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Organize files
for file in os.listdir(folder_dir):
    file_path = os.path.join(folder_dir, file)
    
    if os.path.isfile(file_path):  # Check if it's a file
        for category, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_dir, category))
                break  # Move to the next file

print("✅ Files Organized Successfully!")
