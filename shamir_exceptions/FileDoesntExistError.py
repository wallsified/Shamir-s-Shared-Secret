class FileDoesntExistError(FileNotFoundError):
    """
    Excepción lanzada si el archivo ingresado como
    parámetro no existe o es incorrecto.

   Parámetros
   ----------
        message -- Explicación del error
    """

    def __init__(self, message="La Ruta del Archivo Ingresado No Existe. "):
        extra_line = "Favor de Revisar la Dirección Ingresada"
        self.message = message + extra_line
        super().__init__(self.message)
