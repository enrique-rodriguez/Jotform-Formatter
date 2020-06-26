import os


class ExcelCreator:

    def __init__(self, reader, writer, tasks, prefix):
        """Creates a new ExcelCreator instance

        Args:
            reader (ExcelReader): Reads an excel file type.
            writer (ExcelWriter): Writes an excel file type.
            columns ([str]): The columns that need to be changed.
        """

        self.excel_reader = reader
        self.excel_writer = writer
        self.file_prefix = prefix
        self.tasks = tasks

    def create(self, file, destination):
        """Creates a new excel file with the necessary changes.

        Args:
            file (str): The name of the file.
            destination (str): Path to save the file.
        """

        excel = self.excel_reader.read(file)
        filename = self.build_filename(file, destination)

        for task in self.tasks:
            task.execute(excel)

        self.excel_writer.write(excel, filename)

    def build_filename(self, file, destination):
        """Builds the output file name.

        Args:
            file (str): The name of the file.
            destination (str): Path to save the file

        Returns:
            str: The complete path and filename for the given file.
        """

        return os.path.join(destination, self.file_prefix + os.path.basename(file))
