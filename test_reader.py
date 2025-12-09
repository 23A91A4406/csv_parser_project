from custom_csv_reader import CustomCsvReader

file_path = "samples/test.csv"

reader = CustomCsvReader(file_path)

for row in reader:
    print(row)
