from custom_csv_writer import CustomCsvWriter

rows = [
    ['name', 'age', 'city'],
    ['Alice', 30, 'New York, NY'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie "Chuck"', 35, 'Chicago'],
    ['Diana', 28, 'Los Angeles\nCA']
]

writer = CustomCsvWriter("samples/output.csv")
writer.write_rows(rows)

print("CSV written successfully!")
