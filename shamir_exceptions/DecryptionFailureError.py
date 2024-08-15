# TODO: Revisar utilidad de esta excepción
class DecryptionFailureError(Exception):
    """
    Excepción lanzada en caso de que, por alguna
    razón, la desencriptación no se logró.

   Parámetros
   ----------
        message - Explicación del Error.
    """

    def __int__(self):
        extra_line = "Favor de Intentar Nuevamente."
        self.message = "La Desencriptación no se pudo lograr. " + extra_line
        super().__init__(self.message)
