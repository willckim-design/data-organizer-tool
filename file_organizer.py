import os
import shutil
from datetime import datetime


def organize_files_by_type(source_folder):
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            file_extension = file.split(".")[-1]
            target_folder = os.path.join(source_folder, file_extension.upper())
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)


def organize_files_by_date(source_folder):
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            modification_time = os.path.getmtime(file_path)
            folder_name = datetime.fromtimestamp(modification_time).strftime("%Y-%m-%d")
            target_folder = os.path.join(source_folder, folder_name)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)


def main():
    print("Choose an organization method:")
    print("1. Organize by file type")
    print("2. Organize by modification date")
    choice = input("Enter 1 or 2: ")

    source_folder = input("Enter the folder path to organize: ").strip()
    if not os.path.isdir(source_folder):
        print("Invalid folder path!")
        return

    if choice == "1":
        organize_files_by_type(source_folder)
        print("Files organized by type!")
    elif choice == "2":
        organize_files_by_date(source_folder)
        print("Files organized by date!")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
