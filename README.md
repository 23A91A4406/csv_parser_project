# Custom CSV Reader and Writer in Python

## Project Overview
This project implements a **custom CSV reader and writer** in Python from scratch.  
The goal is to understand **low-level CSV parsing and writing**, handling tricky edge cases like:

- Fields containing **commas**  
- Fields containing **double quotes**  
- Fields containing **newlines**  

The reader and writer are compared against Python's built-in `csv` module in terms of **performance**.

---

## Project Structure

csv_parser_project/
├── custom_csv_reader.py # Custom CSV reader class
├── custom_csv_writer.py # Custom CSV writer class
├── benchmark.py # Benchmarking script
├── test_reader.py # Test script for reader
├── test_writer.py # Test script for writer
├── README.md # Project documentation
├── requirements.txt # Python dependencies (if any)
└── samples/ # Folder for test CSV files
├── test.csv
└── output.csv
