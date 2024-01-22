import csv
from datetime import datetime
import os
import pandas as pd

class CsvWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        # write the headers to the CSV file
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + self.headers)

    def append_data(self, data):
        if not isinstance(data, list):
            data = [data]

        # append data to the CSV file
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + data)

    def delete_row(self, row_index):
        # read the CSV file into a list of rows
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            rows = [row for row in reader]

        # delete the specified row
        del rows[row_index]

        # write the updated rows back to the CSV file
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)

    def delete_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"The file {self.filename} has been deleted.")
        else:
            print(f"The file {self.filename} does not exist.")

    def find_and_replace(self, old_value, new_value):
        # read the CSV file into a list of rows
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            rows = [row for row in reader]

        # replace the old value with the new value
        for row in rows:
            for i, value in enumerate(row):
                if value == old_value:
                    row[i] = new_value

        # write the updated rows back to the CSV file
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)

    def read_csv(self, row=None, column=None):
        df = pd.read_csv(self.filename)

        if row is not None:
            return df.iloc[row].values.tolist()

        if column is not None:
            return df.iloc[:, column].values.tolist()

        return None

    def average(self, column):
        df = pd.read_csv(self.filename)
        return df[column].mean()

    def maximum(self, column):
        df = pd.read_csv(self.filename)
        return df[column].max()

    def minimum(self, column):
        df = pd.read_csv(self.filename)
        return df[column].min()

    def median(self, column):
        df = pd.read_csv(self.filename)
        return df[column].median()

    def variance(self, column):
        df = pd.read_csv(self.filename)
        return df[column].var()

    def std_deviation(self, column):
        df = pd.read_csv(self.filename)
        return df[column].std()

    def variability(self, column):
        df = pd.read_csv(self.filename)
        return df[column].max() - df[column].min()

    def percent_change(self, column):
        df = pd.read_csv(self.filename)
        return df[column].pct_change() * 100
