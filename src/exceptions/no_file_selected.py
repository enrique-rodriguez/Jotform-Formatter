

class NoFileSelected(Exception):
    def __init__(self):
        super().__init__("No se seleccionaron archivos")
