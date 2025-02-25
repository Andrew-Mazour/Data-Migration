# CSV Data Processing Script

## 🔍 Overview

This Python script processes CSV files by performing a series of data transformations and enhancements. It streamlines data cleaning and formatting, making it ideal for preparing data for further analysis or reporting.

## ✨ Features

**Reads CSV Data**: Converts CSV contents into a list of lists.

**Removes Empty Rows**: Cleans up any empty or whitespace-only rows.

**Data Transformations**:

Converts US currency values to Canadian dollars.

Abbreviates transaction types ("Debit" → "DB", "Credit" → "CR").

Splits full names into first and last names.

Validates email addresses.

Cleans and formats phone numbers.

**Sorting Options**: Allows sorting by Transaction ID, Customer ID, or First Name.

**Saves Processed Data**: Outputs the cleaned and formatted data to a new CSV file.

## ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/Data-Migration.git
cd Data-Migration

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

## 🚀 Usage

Place the CSV file to be processed in the project directory.

Run the script:

python main_script.py input.csv output.csv

Choose a sorting option when prompted.


## ⚠️ Disclaimer

Ensure that input CSV files follow a consistent format to avoid processing errors.
