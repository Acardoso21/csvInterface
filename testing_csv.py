from csv_interface import CsvWriter
headers=['header1', 'header2', 'header3']
test = CsvWriter("testingfile.csv", headers)
test.append_data("data_append")
test.append_data("data2")
test.delete_row(1)
test.find_and_replace('data2', 'data3')
test.delete_file()