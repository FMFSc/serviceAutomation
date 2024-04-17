"""
Author: Fellipe Scirea
Version: 1.0
Objective: This class will handle the input provided as a file path, and call individual classes as necessary.
"""

import os

from FilePathParser import FilePathParser


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

class Main:


    if __name__ == '__main__':
        main()
