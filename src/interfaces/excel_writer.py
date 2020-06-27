import abc


class ExcelWriter(abc.ABC):

    @abc.abstractmethod
    def write(self):
        pass
