class MorePartsThanDivisionsError(ValueError):
    """
    Excepción lanzada en caso de que querer recuperar
    un archivo con más partes de las que fue divido

   Parámetros
   ----------
        message - Explicación del error.
    """

    def __init__(self):
        self.message = "No se Puede Recuperar un archivo con más partes de las que fue dividido"
        super().__init__(self.message)
