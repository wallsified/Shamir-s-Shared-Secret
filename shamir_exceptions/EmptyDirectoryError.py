class EmptyDirectoryError(Exception):
    """
    Excepción lanzada si el directorio con las
    n-partes del algoritmo de Shamir está vacío.

   Parámetros
   ----------
        message - Explicación del Error
    """

    def __init__(self, message="El Directorio Ingresado está Vacío. "):
        extra_line = "Verifica que la Ruta Ingresada es la Correcta."
        self.message = message + extra_line
        super().__init__(self.message)
