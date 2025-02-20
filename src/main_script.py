import csv
from csv import reader


class CSVReading:

    def __init__(self, file_dir, encoding="utf-8-sig"):

        self.file_dir = file_dir
        self.encoding = encoding
        self.data = self.read_csv()

    def read_csv(self):
        # Read CSV and convert to a list of lists.
        try:
            with open(self.file_dir, encoding=self.encoding) as file:
                return list(reader(file))
        except FileNotFoundError:
            print(f"File cannot be found: {self.file_dir}")
            return []
        except Exception as e:
            print(f"Error loading the file: {e}")
            return []

    def remove_empty_list(self):
        # Remove the last row (list) if it is empty or consists of whitespace strings.

        if self.data and not any(cell.strip() for cell in self.data[-1]):
            self.data.pop()

    def data_changes(self):
        # All changes made to the data that are done in the DataChanger class.

        changer = DataChanger(self.data)
        changer.currency_converter()
        changer.convert_transaction_type()
        changer.split_full_name()
        changer.validate_email()
        changer.mod_phone_numbers()
        self.data = changer.data

    def sorting_types(self):
        # Providing the choice for the user to select soring type.

        print("(1 - Transaction ID)\n(2 - Customer ID)\n(3 - First Name)")
        sort_type = input("Select sorting method: ")

        if sort_type == "1":
            self.data.sort(key=lambda row: int(row[1].strip()))
        elif sort_type == "2":
            self.data.sort(key=lambda row: int(row[7].strip()))
        elif sort_type == "3":
            self.data.sort(key=lambda row: row[8].strip().lower())
        else:
            print("Please select a valid sorting type")
            
        #Ensures data is safely transfered/saved in new CSV file
    def save_to_new_csv(self, output_file_dir):
        try:
            with open(output_file_dir, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.data)
        except Exception as e:
            print(f"Error saving file: {e}")

    def process(self, output_file_dir):
        # Calling all previous functions.

        self.remove_empty_list()
        self.data_changes()
        self.sorting_types()
        self.save_to_new_csv(output_file_dir)


class DataChanger:

    def __init__(self, data):
        self.data = data

    def currency_converter(self):
        # Substitute desired currency and row index.

        for row in self.data:
            if row[4] == "US":
                try:
                    row[3] = round(float(row[3]) * 1.39, 2)
                    row[4] = "Cnd"
                except ValueError:
                    print(f"Invalid currency value: {row[3]}")

    def convert_transaction_type(self):
        # Substitute desired short-form and index.

        for row in self.data:
            if row[6] == "Debit":
                row[6] = "DB"
            elif row[6] == "Credit":
                row[6] = "CR"

    def split_full_name(self):
        # Substitute desired index.

        for row in self.data:
            names = row[8].split(maxsplit=1)
            if len(names) == 2:
                first_name, last_name = names
            else:
                first_name, last_name = names[0], ''
            row[8] = first_name
            row.insert(9, last_name)

    def validate_email(self):
        # Can include other types of characters.
        # Substitute desired index.

        for row in self.data:
            if "@" not in row[-2]:
                row[-2] = "Invalid"

    def mod_phone_numbers(self):
        # Can change modified characters.
        # Substitute desired index.

        for row in self.data:
            row[-1] = ''.join(char for char in row[-1] if char.isdigit())


if __name__ == "__main__":
    input_file = "unmodified.csv"  # Enter old CSV path here
    output_file = "modified.csv"  # Enter new CSV path here

    processor = CSVReading(input_file)
    processor.process(output_file)  # process() executes all functions.

# If necessary, include input statement to avoid .exe closing (ex. input("Press enter to exit"))
