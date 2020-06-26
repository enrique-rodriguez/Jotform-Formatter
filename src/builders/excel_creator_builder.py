from adapters import ExcelCreator
from usecases import ModifyColumnsWithValue, AddNumbersColumn

from config.configuration import (
    excel_reader,
    excel_writer
)
from config.columns import (
    COLUMNS_TO_MODIFY,
    REPLACEMENT_TEXT
)
from config.constants import FILE_PREFIX


class ExcelCreatorBuilder:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def build_columns_task(self):
        add_columns_task = ModifyColumnsWithValue(
            COLUMNS_TO_MODIFY, REPLACEMENT_TEXT
        )

        self.add_task(add_columns_task)

    def build_add_numbers_task(self):
        self.add_task(AddNumbersColumn())

    def build(self):

        return ExcelCreator(
            reader=excel_reader(),
            writer=excel_writer(),
            tasks=self.tasks,
            prefix=FILE_PREFIX
        )
