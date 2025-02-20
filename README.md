# Data Migration Project

## Description
This Python script processes CSV files by performing a series of data transformations and enhancements. It begins by reading the CSV file and converting its contents into a list of lists.
The script then removes any empty or whitespace-only rows from the end of the data. Following this, it applies various modifications: converting US currency values to Canadian dollars (as an example),
abbreviating transaction types from "Debit" and "Credit" to "DB" and "CR" respectively, splitting full names into first and last names, validating email addresses, and cleaning phone numbers.

Users can select a sorting method for the data, with options including sorting by Transaction ID, Customer ID, or First Name. Finally, the processed data is saved to a new CSV file.
The script is designed to streamline data cleaning and formatting tasks, making it ideal for preparing data for further analysis or reporting.

## Structure
- **src/**: Contains the main Python script for processing the CSV data.
  - `main_script.py`: The main script that handles reading, modifying, sorting, and saving the CSV data.

- **tests/**: Contains unit tests for validating the functionality of the scripts.
  - `test_main_script.py`: Unit tests for the functions and methods in `main_script.py`.

- **data/**: Contains sample CSV files used for testing and demonstration.
  - `unmodified.csv`: Example of an unmodified CSV file for processing.
  - `modified.csv`: Example of a processed CSV file after modifications.

- **README.md**: Provides a description of the project and information about the repository.

## Running the Tests
Navigate to the `tests/` directory and run the following command: python -m unittest discover 
