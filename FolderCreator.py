"""
Author: Fellipe Scirea
Version: 1.0
Objective: This class creates folders based on parsed information such as customer name, job number, and job description.
"""

import os


class FolderCreator:
    """Class to create folders based on the provided file path."""

    def __init__(self, base_path):
        self.base_path = base_path

    def create_folders(self, process_type):
        """Create folders based on the process type."""
        # Define folder names based on process type
        if process_type == "Field Service":
            folder_names = ["RMA", "Site Pictures", "Tear-down Pictures", "Work Orders"]
        elif process_type == "Repair":
            folder_names = ["RMA", "Tear-down Pictures", "Work Orders"]
        else:
            folder_names = ["Work Orders"]

        # Create folders
        for folder_name in folder_names:
            folder_path = os.path.join(self.base_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
