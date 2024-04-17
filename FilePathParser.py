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
        # Split the file path into parts using backslashes
        parts = self.file_path.split("\\")

        # Find the index of "Customers"
        customers_index = parts.index("Customers")

        # Extract customer name
        customer_name = parts[customers_index + 1]

        # Extract job number and process name
        job_number_and_process = parts[customers_index + 2]
        job_number = job_number_and_process[:5]  # First 5 characters are job number
        # Extract job number and process name
        job_number_and_process = parts[customers_index + 2]
        job_number = job_number_and_process[:5]  # First 5 characters are job number

        # Extract process name (everything after "Field Service" or "Repair")
        process_index = job_number_and_process.find("Field Service")
        if process_index == -1:
            process_index = job_number_and_process.find("Repair")
        process_name = job_number_and_process[process_index+len("Field Service"):].strip() if process_index != -1 else "Unknown"

        # Determine the type of process (Field Service or Repair)
        process_type = "Field Service" if "Field Service" in job_number_and_process else "Repair" if "Repair" in job_number_and_process else "Unknown"

        return customer_name, job_number, process_type, process_name.strip()  # Strip to remove leading/trailing spaces
