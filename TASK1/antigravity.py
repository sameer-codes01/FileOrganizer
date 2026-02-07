import os
import shutil
from pathlib import Path

# Define the directory to organize (Change this to your path)
# Use Path.home() / "Downloads" for a cross-platform way to get the Downloads folder
TARGET_DIR = Path.home() / "Downloads"

# Category mapping: Folder Name -> List of extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts_Executables": [".py", ".exe", ".sh", ".msi"],
}

def organize_files():
    # Ensure the directory exists
    if not TARGET_DIR.exists():
        print(f"Error: The directory {TARGET_DIR} does not exist.")
        return

    print(f"Organizing files in: {TARGET_DIR}...")

    for item in TARGET_DIR.iterdir():
        # Skip directories, we only want to move files
        if item.is_dir():
            continue
        
        # Determine the category based on extension
        file_ext = item.suffix.lower()
        dest_folder = "Others" # Default folder

        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                dest_folder = category
                break

        # Create the destination folder path
        dest_path = TARGET_DIR / dest_folder
        dest_path.mkdir(exist_ok=True)

        # Move the file
        try:
            shutil.move(str(item), str(dest_path / item.name))
            print(f"Moved: {item.name} -> {dest_folder}/")
        except Exception as e:
            print(f"Could not move {item.name}: {e}")

    print("\nCleanup complete!")

if __name__ == "__main__":
    organize_files()