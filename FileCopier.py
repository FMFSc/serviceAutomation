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

    def copy_files(self, process_type):
        """Copy files based on the process type."""
        # Define source and destination directories
        source_dir = self.source_path
        destination_dir = self.destination_path

        # Define file paths based on process type
        if process_type == "Repair":
            rma_file = "AWC RMA Request Form.docx"
            proposal_file = "AWC Inspection Report #.docx"
            work_order_files = ["Inspection Work Order #.xlsx", "Assembly Work Order #.xlsx"]
        elif process_type == "Field Service":
            rma_file = "AWC RMA Request Form.docx"
            proposal_file = "AWC Field Service Report #.docx"
            work_order_files = ["Field Service Work Order #.xlsx", "Inspection Work Order #.xlsx",
                                "Assembly Work Order #.xlsx"]
        else:
            # Default values if process type is unknown
            rma_file = ""
            proposal_file = ""
            work_order_files = []

        # Copy files to respective folders
        shutil.copy2(os.path.join(source_dir, rma_file), os.path.join(destination_dir, "RMA", rma_file))
        shutil.copy2(os.path.join(source_dir, proposal_file), os.path.join(destination_dir, "Proposal", proposal_file))
        for work_order_file in work_order_files:
            shutil.copy2(os.path.join(source_dir, work_order_file),
                         os.path.join(destination_dir, "Work Orders", work_order_file))
