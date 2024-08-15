class InvalidNameError(ValueError):
    """
    Excepción lanzada en caso de que el nombre
    del archivo de salida sea inválido. Esto es
    por ejemplo, si tiene comas en el nombre del
    archivo.

   Parámetros
   ----------
        message - Explicación del Error
    """

    def __init__(self, file_name: str):
        first_line = f"El nombre {file_name} es inválido. "
        self.message = first_line + "Intenta con un nombre con solo caractéres alfanuméricos."
        super().__init__(self.message)
