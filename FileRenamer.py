"""
Author: Fellipe Scirea
Version: 1.0
Objective: This class renames files based on specified new names.
"""

import os


class FileRenamer:
    """Class to rename files based on the provided job number."""

    def __init__(self, destination_path, job_number):
        self.destination_path = destination_path
        self.job_number = job_number

    def rename_files(self):
        """Rename copied files by inserting job number."""
        # Define destination directory
        destination_dir = self.destination_path

        for root, _, files in os.walk(destination_dir):
            for file_name in files:
                if '#' in file_name:
                    source_file_path = os.path.join(root, file_name)
                    new_file_name = file_name.replace('#', f'#{self.job_number}')
                    new_file_path = os.path.join(root, new_file_name)
                    print(f"Renaming '{file_name}' to '{new_file_name}'")
                    os.rename(source_file_path, new_file_path)
                    print("File renamed successfully.")