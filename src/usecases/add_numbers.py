from interfaces import Task


class AddNumbersColumn(Task):
    """Adds a number column to the excel file."""

    def execute(self, excel):
        """Adds the numbers column to the given excel sheet.

        Args:
            excel (DataFrame): The excel file
        """
        self.add_numbers(excel)

    def add_numbers(self, excel):
        """Adds indexes column to the first row in the excel spreadsheet.

        Args:
            excel (DataFrame): Excel file in DataFrame data type.
        """

        numbers = [i for i in range(1, len(excel.index)+1)]
        excel.insert(0, '#', numbers, True)
