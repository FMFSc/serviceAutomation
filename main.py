"""
Author: Fellipe Scirea
Version: 1.0
Objective: This class will handle the input provided as a file path, and call individual classes as necessary.
"""

import os

from FileCopier import FileCopier
from FilePathParser import FilePathParser
from FolderCreator import FolderCreator


def get_file_path_from_user():
    """Prompt the user to input a file path."""
    file_path = input("Enter the file path: ")
    return file_path

def main():
    """Main function."""
    # get file path from user
    file_path = get_file_path_from_user()

    #Instantiate FilePathParser class
    parser = FilePathParser(file_path)
    customer_name, job_number, process_type, process_name = parser.parse()


    # Print the parsed information
    print("Customer Name:", customer_name)
    print("Job Number:", job_number)
    print("Process Type:", process_type)
    print("Process Name:", process_name)

    # Instantiate FolderCreator class
    base_path = file_path  # Your base path here
    creator = FolderCreator(base_path)

    # Create folders based on the process type
    creator.create_folders(process_type)

    print("Folders created successfully.")

    # Instantiate FileCopier class
    source_path = r"C:\Users\Fellipes\Documents\serviceAutomation"
    destination_path = file_path
    copier = FileCopier(source_path, destination_path)

    # Copy files based on the process type
    copier.copy_files(process_type)

    print("Files copied successfully.")


class Main:


    if __name__ == '__main__':
        main()
