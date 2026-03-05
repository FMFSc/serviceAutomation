# serviceAutomation

# serviceAutomation

A small Python CLI tool that automates service job folder setup and template document preparation.

Given a job folder path, it:
1. Parses the path to extract customer name, job number, and process type (Field Service or Repair)
2. Creates a standard folder structure based on the process type
3. Copies predefined template files into the correct folders
4. Renames copied files by replacing `#` with `#<job_number>`

This is designed around a specific Windows directory convention used for service jobs.

## What is implemented today

### Folder creation
Creates folders under the provided job path:
- Field Service: `RMA`, `Site Pictures`, `Tear-down Pictures`, `Work Orders`
- Repair: `RMA`, `Tear-down Pictures`, `Work Orders`
- Other: `Work Orders`

## Template copying
Copies template documents from a source templates directory into the new folders.
The templates differ by process type (Repair vs Field Service) and include work order spreadsheets.

## File renaming
Walks all files under the destination job folder and renames any file containing `#` by inserting the job number, for example:
- `AWC RMA Request Form #.docx` becomes `AWC RMA Request Form #12345.docx`

## Requirements

- Python 3.x
- Windows is assumed (path parsing uses backslashes and expects a Windows style folder structure)
- Template files must exist in your templates directory (see Configuration)

## Configuration (important)

This repo currently contains hardcoded paths in `Main.py` that you must change for your machine:
- `source_path` points to the folder that contains the template files
- `destination_path` is the job folder path you enter when prompted

In `Main.py`, update this line to the folder where your templates live:

```python
source_path = r"C:\Users\Fellipes\Documents\serviceAutomation"
