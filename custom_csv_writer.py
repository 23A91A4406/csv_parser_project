class CustomCsvWriter:
    """
    A custom CSV writer that writes rows of data to a CSV file,
    correctly quoting fields when needed.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def _quote_field(self, field):
        """
        Check if a field needs quotes.
        Escape existing quotes by doubling them.
        """
        field = str(field)
        if any(char in field for char in [',', '"', '\n']):
            field = field.replace('"', '""')  # Escape quotes
            field = f'"{field}"'              # Wrap in quotes
        return field

    def write_rows(self, rows):
        """
        Write a list of rows (lists) to a CSV file.
        """
        with open(self.file_path, 'w', encoding='utf-8') as f:
            for row in rows:
                quoted_row = [self._quote_field(cell) for cell in row]
                line = ','.join(quoted_row)
                f.write(line + '\n')
