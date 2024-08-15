class FewDivisionsError(ValueError):
    """
    Excepción lanzada si la cantidad de
    divisiones es menor a la mínima, 3.

   Parámetros
   ----------
        message - Explicación del Error
        divisions - Número de Divisiones ingresado.
    """

    def __init__(self, divisions: int, message="El número de divisiones debe ser mayor a 3."):
        self.divisions = divisions
        extra_line = f"Ingresaste {self.divisions} divisiones como parámetro. "
        self.message = extra_line + message
        super().__init__(self.message)

