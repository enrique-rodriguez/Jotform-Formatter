from tkinter import *
from tkinter.ttk import *

from tkinter import messagebox, filedialog
from tkinter.filedialog import askopenfilenames

from exceptions import (
    NoFileSelected,
    DirectoryNotSpecified,
    InvalidFormat
)

from config.errors import (
    UNEXPECTED_ERROR_MESSAGE,
)

from builders import ExcelCreatorBuilder


class Application(Frame):
    """GUI Application Wrapper"""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.destination = None
        self.files = []

        self.dest_text = StringVar(
            master=self.master, value='Destino: No especificado'
        )

        self.total_selected = StringVar(
            self.master,
            value='0 archivos seleccionados'
        )

        self.add_numbers = BooleanVar(self.master, value=True)

        self.add_numbers_checkbox = Checkbutton(
            self.master,
            text="Añadir números",
            variable=self.add_numbers
        )

        self.modify_columns = BooleanVar(self.master, value=True)

        self.modify_columns_checkbox = Checkbutton(
            self.master,
            text="Modificar columnas",
            variable=self.modify_columns
        )

        self.total_selected_label = Label(
            self.master,
            textvariable=self.total_selected
        )

        self.dest_label = Label(
            master=self.master,
            textvariable=self.dest_text
        )

        self.open_button = Button(
            self.master, text='Seleccionar',
            command=self.choose_files_handler
        )

        self.dest_button = Button(
            self.master, text='Salvar a',
            command=self.dest_button_handler
        )

        self.create_button = Button(
            self.master, text="Crear Excels",
            command=self.create_excels_handler,
            style='W.TButton', state=DISABLED
        )

        self.arrange_ui()

    def arrange_ui(self):
        """Places buttons and labels on the GUI"""

        self.dest_button.pack()
        self.dest_label.pack()
        self.open_button.pack()
        self.total_selected_label.pack()
        self.add_numbers_checkbox.pack()
        self.modify_columns_checkbox.pack()
        self.create_button.pack()

    def dest_button_handler(self):
        """Method that gets executed when the destination button is pressed."""

        self.destination = filedialog.askdirectory()
        self.dest_text.set(f"Destino: {self.destination}")

    def create_excels_handler(self):
        """Method that gets executed when the create button is pressed."""

        try:
            self.create_excels()
        except (NoFileSelected, DirectoryNotSpecified, InvalidFormat) as error:
            self.display_error(error)
        except Exception as error:
            self.display_error(
                UNEXPECTED_ERROR_MESSAGE.format(error=error)
            )

    def display_error(self, message):
        """Displays a given error message

        Args:
            message (str): The error message to display.
        """

        messagebox.showerror("Error", message)

    def display_success(self, message):
        """Displays a given success message

        Args:
            message (str): The success message to display.
        """

        messagebox.showinfo("Éxito", message)

    def create_excels(self):
        """Create excel for every file in the buffer

        Raises:
            NoFileSelected: Error when no file is selected.
            DirectoryNotSpecified: Error when directory not specified.
        """

        if len(self.files) < 1:
            raise NoFileSelected()

        if self.destination == None:
            raise DirectoryNotSpecified()

        excel_creator = self.get_excel_creator()

        for file in self.files:
            excel_creator.create(file, self.destination)

        self.display_success(
            f"Archivos creados exitosamente\nSe a creado {len(self.files)} archivo/s"
        )

    def get_excel_creator(self):
        """Returns the ExcelCreator instance

        Returns:
            ExcelCreator: Instance of ExcelCreator
        """

        builder = ExcelCreatorBuilder()

        if self.modify_columns.get():
            builder.build_columns_task()

        if self.add_numbers.get():
            builder.build_add_numbers_task()

        return builder.build()

    def choose_files_handler(self):
        """Method that gets executed when the choose files button is pressed."""

        files = askopenfilenames(title="Seleccionar Excels")

        if len(files) < 1:
            return

        self.files = files
        self.total_selected.set(f"{len(self.files)} archivos seleccionados")

        state = NORMAL if (len(self.files) and self.destination) else DISABLED

        self.create_button.config(state=state)
