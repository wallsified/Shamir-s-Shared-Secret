class IncorrectPassWordError(ValueError):
    """
    Excepción lanzada en caso de intentar descifrar
    con una contraseña incorrecta

   Parámetros
   ----------
        message - Explicación del Error
    """

    def __init__(self, message="La Contraseña Ingresada Para Descifrar es Incorrecta. "):
        extra_line = "Favor de Intentar de nuevo."
        self.message = message + extra_line
        super().__init__(self.message)
