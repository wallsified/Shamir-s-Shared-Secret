"""
Validación del input ingresado para encriptar
un archivo

Autor: @wallsified
Version: 1.0
"""

from os import path
import shamir_exceptions
from getpass import getpass
from hashlib import sha256


def validate_input(input_path: str, file_name: str, divisions: int, minimum_parts: int) -> (str, str, int, int, bytes):
    """
    Método validador del input ingresado para encriptar un archivo.

   Parámetros
   ----------
        input_path - str. Ruta del Archivo a Encriptar.
        file_name - str. Nombre del Archivo Encriptado
        divisions - int. Número de Divisiónes para la Encriptación.
        minimum_parts - int. Número de Partes Mínimas para la Desencriptación.

    Regresa
    -------
        input_path - str. Ruta del Archivo a Encriptar.
        file_name - str. Nombre del Archivo Encriptado
        divisions - int. Número de Divisiónes para la Encriptación.
        minimum_parts - int. Número de Partes Mínimas para la Desencriptación.
        password - bytes. Contraseña a usar en la Encriptación.
    """

    password = ""
    try:
        if path.exists(input_path) is False:
            raise shamir_exceptions.FileDoesntExistError()
        elif divisions <= 3:
            raise shamir_exceptions.FewDivisionsError(divisions)
        elif minimum_parts <= 4:
            raise shamir_exceptions.FewMinimumParts()
        elif minimum_parts >= divisions:
            raise shamir_exceptions.MorePartsThanDivisionsError()
        elif file_name.isalpha() is False:
            raise shamir_exceptions.InvalidNameError(file_name)
        else:
            password = getpass("\n--- Introduce una Contraseña para Cifrar: ")
            if len(password) < 8:
                raise shamir_exceptions.UnsecurePasswordError()
            else:
                password = password.encode('utf-8')
                password = sha256(password).digest()
    except ValueError as error:
        print(f"{error}\n")

    print("\nArgumentos Ingresados Válidados. Iniciando Proceso de Encriptación\n")

    return input_path, file_name, divisions, minimum_parts, password
