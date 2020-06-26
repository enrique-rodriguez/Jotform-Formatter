import abc


class ExcelReader(abc.ABC):

    @abc.abstractmethod
    def read(self):
        pass
