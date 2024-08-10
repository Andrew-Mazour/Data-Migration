import unittest
import os
import csv
from main_script import CSVReading, DataChanger


class TestCSVReading(unittest.TestCase):

    @classmethod
    def create_class(cls):
        # Substitute with input/output file path
        cls.input_file = 'unmodified.csv'
        cls.output_file = 'modified.csv'

    def create_instance(self):
        # Create the instance to use for each test
        self.processor = CSVReading(self.input_file)

    def test_read_csv(self):
        # Ensures data exists and was loaded from CSV file
        self.assertGreater(len(self.processor.data), 0, "Data must be loaded from CSV")

    def test_remove_empty_list(self):
        # Record original length
        original_length = len(self.processor.data)

        # Manually add various types of empty rows to test if the remove_empty_list function will remove empty lists.
        # If not, original_length + 3 will be equal to (len(self.processor.data).

        self.processor.data.append([])  # Empty list
        self.processor.data.append([''])  # List with empty string
        self.processor.data.append(['', ''])  # List with two empty strings

        # Call remove_empty_list function.
        self.processor.remove_empty_list()

        # Assert the length of data has decreased, meaning an empty row was removed
        self.assertLess(len(self.processor.data), original_length + 3, "Empty rows have not been removed")

    def test_data_changes(self):
        # Avoid index error by ensuring there are enough columns (my CSV had 11 columns or 10 indices).
        for row in self.processor.data:
            if len(row) < 11:  # Make sure we have enough columns to avoid index errors
                row.extend([''] * (11 - len(row)))

        initial_data_length = len(self.processor.data)
        self.processor.data_changes()
        self.assertEqual(len(self.processor.data), initial_data_length,
                         "Data length should not change after transformation")

    def test_save_to_new_csv(self):
        self.processor.save_to_new_csv(self.output_file)
        # Verifies that file exists
        self.assertTrue(os.path.exists(self.output_file), "Output file should be created")

        with open(self.output_file, 'r') as file:
            reader = csv.reader(file)
            output_data = list(reader)
        # Verifies that new CSV file data matches transformed old CSV file data.
        self.assertEqual(output_data, self.processor.data, "Output data should match processed data")

    # Refers to class itself (where output_file is defined). Deletes file after test to avoid traffic

    @classmethod
    def tearDownClass(cls):
        # Clean up the output file if needed
        if os.path.exists(cls.output_file):
            os.remove(cls.output_file)


class TestDataChanger(unittest.TestCase):

    def create_sample(self):
        # Sample data for testing. Each function is tested on sample data.
        self.data = [
            ['1', '100', '2024-04-21', '100.00', 'US', '', 'Debit', '',
             'Jane Smith', 'janesmith@example.com', '123-456-7890']
        ]
        # Create instance for testing.
        self.changer = DataChanger(self.data)

    def test_currency_converter(self):
        self.changer.currency_converter()
        if len(self.data[0]) > 4:  # Ensure we don't run into index errors (currency abbr. on 4th index).
            self.assertEqual(self.data[0][4], 'Cnd', "Currency should be converted to Cnd")
            self.assertAlmostEqual(float(self.data[0][3]), 139.00, places=2,
                                   msg="Currency value should be converted correctly")

    def test_convert_transaction_type(self):
        self.changer.convert_transaction_type()
        if len(self.data[0]) > 6:  # Transaction type on 6th index.
            self.assertEqual(self.data[0][6], 'DB', "Transaction type should be changed to DB")

    def test_split_full_name(self):
        self.changer.split_full_name()
        if len(self.data[0]) > 8:  # Full name on 8th index.
            self.assertEqual(self.data[0][8], 'Jane', "First name should be correctly split")
            self.assertEqual(self.data[0][9], 'Smith', "Last name should be correctly split")

    def test_validate_email(self):
        self.data[0][-2] = 'invalid_email'
        self.changer.validate_email()
        if len(self.data[0]) > 9:  # Email on 9th index.
            self.assertEqual(self.data[0][-2], 'Invalid', "Invalid emails should be marked as 'Invalid'")

    def test_mod_phone_numbers(self):
        self.changer.mod_phone_numbers()
        if len(self.data[0]) > 10:  # Phone numbers on 10th index.
            self.assertEqual(self.data[0][-1], '1234567890', "Phone numbers should be modified correctly")


if __name__ == "__main__":
    unittest.main()
