class UnsecurePasswordError(ValueError):
    """
    Excepción lanzada si la contraseña ingresada no
    tiene la longitud deseada o no posee características
    válidas.

   Parámetros
   ----------
        message - Explicación del Error
    """

    def __init__(self, message="La contraseña ingresada no es segura. "):
        extra_line = "Intenta con una contraseña más larga o del tipo 's3GuR$' "
        self.message = message + extra_line
        super().__init__(self.message)
