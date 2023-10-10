import os
import shutil
import time

# Prompt user for folder path that needs to be sorted
source_folder = input("Enter your Download/source folder path: ")

# Define file extensions and their corresponding folders
extensions_to_folders = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".png": "Images",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".mp4": "Videos",
    ".mp3": "Music",
    ".zip": "Archives",
    ".pptx": "PowerPoint",
}


def sort_files():
    for filename in os.listdir(source_folder):
        # Join source folder path with file name
        source_file = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_file):
            # Get file ext
            _, extension = os.path.splitext(filename)

            # Get extension folder
            destination_folder = extensions_to_folders.get(extension, "Other")

            # Create the destination folder path
            destination_folder_path = os.path.join(source_folder, destination_folder)

            # Create the destination folder if it doesn't exist
            os.makedirs(destination_folder_path, exist_ok=True)

            # Move file
            destination_file_path = os.path.join(destination_folder_path, filename)
            shutil.move(source_file, destination_file_path)

            print(f"Successfully moved '{filename}' to '{destination_folder}'")


sort_files()

# Keep running
while True:
    condition = input("Do you want to sort again?(Y/N): ")
    if condition == "Y" or condition == "y":
        sort_files()
    else:
        break
