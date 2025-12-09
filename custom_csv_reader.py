class CustomCsvReader:
    """
    A custom CSV reader that reads CSV files character-by-character
    and correctly handles commas, quotes, escaped quotes, and newlines.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, "r", encoding="utf-8")
        self.buffer = ""  # stores characters for the current cell
        self.in_quotes = False  # tracks whether we are inside quotes

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        self.buffer = ""
        self.in_quotes = False

        while True:
            char = self.file.read(1)

            if not char:
                # End of file
                if self.buffer:
                    row.append(self.buffer)
                    return row
                self.file.close()
                raise StopIteration

            # If the character is a quote
            if char == '"':
                if self.in_quotes:
                    # Peek next char to check escaped quote
                    next_char = self.file.read(1)
                    if next_char == '"':
                        # Escaped quote
                        self.buffer += '"'
                    else:
                        # End of quoted field
                        self.in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    # Entering a quoted field
                    self.in_quotes = True

            # If the character is a comma and we are NOT inside quotes → end of cell
            elif char == "," and not self.in_quotes:
                row.append(self.buffer)
                self.buffer = ""

            # If the character is a newline and we are NOT inside quotes → end of row
            elif char == "\n" and not self.in_quotes:
                row.append(self.buffer)
                return row

            else:
                # Normal character
                self.buffer += char
