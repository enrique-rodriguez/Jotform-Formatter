import pandas
import xlrd

from interfaces import ExcelReader
from exceptions import InvalidFormat


class PandasExcelReader(ExcelReader):

    def read(self, file):
        try:
            return pandas.read_excel(file)
        except xlrd.XLRDError as error:
            """Raise our own exception to decouple from the xlrd library."""
            raise InvalidFormat
