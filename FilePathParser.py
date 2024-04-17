"""
    Author: Fellipe Scirea
    Version: 1.0
    Objective: This class parses file paths and extracts relevant information such as customer name, job number, and job description.
    """


class FilePathParser:
    """Class to parse file paths and extract relevant information."""

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        """Parse the file path and extract customer name, job number, and job description."""
        parts = self.file_path.split(os.path.sep)
        customer_name = parts[-3]
        job_number = parts[-2]
        job_description = parts[-1]
        return customer_name, job_number, job_description
