

class InvalidFormat(Exception):
    def __init__(self):
        super().__init__("El formato del archivo es invalido.")
