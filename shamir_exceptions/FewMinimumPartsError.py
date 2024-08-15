class FewMinimumParts(ValueError):
    """
    Excepción lanzada en caso de que el total
    de las partes mínimas para la reconstrucción
    del archivo es menor a 4.

   Parámetros
   ----------
        message: Explicación del Error
    """

    def __init__(self):
        first_line = f"El número de partes ingresadas debe ser mayor a 4. "
        self.message = first_line + "Favor de Intentar con un número mayor"
        super().__init__(self.message)
