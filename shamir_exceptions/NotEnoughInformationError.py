class NotEnoughInformationError(Exception):
    """
    Excepción lanzada en caso de que alguna de las
    partes para descifrar un archivo contenga menos
    de 3 líneas.

   Parámetros
   ----------
        message - Explicación del Error
    """

    def __init__(self, file_name: str):
        self.message = f"El archivo {file_name} no contiene información suficiente para descifrar."
        super().__init__(self.message)
