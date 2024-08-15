class IncorrectFileTypeError(FileNotFoundError):
    """
    Excepción lanzada en caso de ingresar un archivo
    cuya extensión no es ".aes" al momento de descifrar.

   Parámetros
   ----------
        message - Explicación del Error.
    """

    def __init__(self, input_path: str):
        first_line = f"El archivo {input_path} ingresado no es del Tipo Correcto. "
        self.message = first_line + "Favor de revisar la ruta ingresada."
        super().__init__(self.message)
