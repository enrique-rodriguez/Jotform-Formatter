import pandas

from interfaces import ExcelWriter


class PandasExcelWriter(ExcelWriter):

    def write(self, frame, file):

        with pandas.ExcelWriter(file) as writer:
            frame.to_excel(writer)
