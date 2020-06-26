

class DirectoryNotSpecified(Exception):
    def __init__(self):
        super().__init__("Directorio de destino no especificado")
