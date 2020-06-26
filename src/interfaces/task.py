import abc


class Task(abc.ABC):
    """Executes a task on an Excel File"""

    @abc.abstractmethod
    def execute(self, excel):
        pass
