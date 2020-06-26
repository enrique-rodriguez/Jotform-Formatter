from interfaces import Task


class ModifyColumnsWithValue(Task):

    def __init__(self, columns, value):
        self.columns_to_modify = columns
        self.value = value

    def execute(self, excel):
        """Modifies the columns in the given excel file.

        Args:
            excel (DataFrame): The excel file
        """

        self.modify_columns(excel)

    def modify_columns(self, excel):
        """Modifies the columns with the replacement text

        Args:
            excel (DataFrame): Excel file in DataFrame data type.
        """

        for column in self.columns_to_modify:
            excel[column] = excel[column].apply(
                lambda x: self.value)
