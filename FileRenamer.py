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

        # Define file names to be renamed based on the job number
        files_to_rename = [
            "AWC RMA Request Form #.docx",
            "AWC Inspection Report #.docx",
            "Field Service Work Order #.xlsx",
            "Inspection Work Order #.xlsx",
            "Assembly Work Order #.xlsx"
        ]

        # Rename each specified file by inserting job number
        for file_name in files_to_rename:
            if os.path.exists(os.path.join(destination_dir, file_name)):
                new_file_name = file_name.replace('#', f'#{self.job_number}')
                os.rename(os.path.join(destination_dir, file_name), os.path.join(destination_dir, new_file_name))
