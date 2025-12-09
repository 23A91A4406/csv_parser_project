import csv
import time
from custom_csv_reader import CustomCsvReader
from custom_csv_writer import CustomCsvWriter

# 1️⃣ Generate synthetic data
rows = [["Name", "Age", "City", "Email", "Country"]]
for i in range(10000):
    rows.append([f"User{i}", str(20 + i % 30), f"City{i % 100}", f"user{i}@example.com", f"Country{i % 50}"])

# 2️⃣ Write CSV using custom writer
start = time.time()
writer = CustomCsvWriter("samples/custom_output.csv")
writer.write_rows(rows)
end = time.time()
print(f"CustomCsvWriter time: {end - start:.4f} seconds")

# 3️⃣ Write CSV using Python's csv.writer
start = time.time()
with open("samples/csv_output.csv", "w", newline="", encoding="utf-8") as f:
    writer_std = csv.writer(f)
    writer_std.writerows(rows)
end = time.time()
print(f"csv.writer time: {end - start:.4f} seconds")

# 4️⃣ Read CSV using custom reader
start = time.time()
reader = CustomCsvReader("samples/custom_output.csv")
for _ in reader:
    pass
end = time.time()
print(f"CustomCsvReader time: {end - start:.4f} seconds")

# 5️⃣ Read CSV using Python's csv.reader
start = time.time()
with open("samples/csv_output.csv", "r", encoding="utf-8") as f:
    reader_std = csv.reader(f)
    for _ in reader_std:
        pass
end = time.time()
print(f"csv.reader time: {end - start:.4f} seconds")
