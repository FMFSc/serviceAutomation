"""
Author: Fellipe Scirea
Version: 1.0
Objective: This class copies specific files from a source directory to a destination directory based on the process name.
"""
import os
import shutil


class FileCopier:
    """Class to copy files based on the provided process type."""

    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

        # Define process_templates dictionary with folder names
        self.process_templates = {
            "Repair": {
                "RMA": "AWC RMA Request Form #.docx",
                "Proposal": "AWC Inspection Report #.docx",
                "Work Orders": "Work Orders"  # String for the folder name
            },
            "Field Service": {
                "RMA": "AWC RMA Request Form #.docx",
                "Proposal": "AWC Field Service Report #.docx",
                "Work Orders": "Work Orders"  # String for the folder name
            }
        }

        # Define work_order_files dictionary (modify based on your process types)
        self.work_order_files = {
            "Repair": ["Assembly Work Order #.xlsx", "Inspection Work Order #.xlsx"],
            "Field Service": ["Field Service Work Order #.xlsx", "Assembly Work Order #.xlsx", "Inspection Work Order #.xlsx"]
        }

    def copy_files(self, process_type):
        """Copy files based on the process type."""

        process_templates = self.process_templates.get(process_type)

        if not process_templates:
            print(f"Invalid process type: {process_type}")
            return

        for folder, file_pattern in process_templates.items():
            destination_folder = os.path.join(self.destination_path, folder)

            if folder == "Work Orders":
                for work_order_file in self.work_order_files[process_type]:
                    source_file = os.path.join(self.source_path, work_order_file)
                    destination_work_order_folder = os.path.join(self.destination_path, folder)
                    os.makedirs(destination_work_order_folder, exist_ok=True)
                    shutil.copy2(source_file, destination_work_order_folder)
                    print(f"Copied {source_file} to {destination_work_order_folder}")
            else:
                source_file = os.path.join(self.source_path, file_pattern)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.copy2(source_file, destination_folder)
                print(f"Copied {source_file} to {destination_folder}")

