"""
Validación del input ingresado para
desencriptar un archivo ingresado, dadas
t-partes (según el secreto compartido de Shamir).

Autor: @wallsified
Version: 1.0
"""

from os import path
import shamir_exceptions
import linecache


def file_has_more_than_two_lines(file_name: str) -> bool:
    """
    Método auxiliar para revisar que un archivo tenga más
    de dos lineas de contenido.

    Parámetros
    ----------
        file_name - str: Nombre del Archivo.

    Regresa
    -------
        bool - True si el archivo contiene más de dos lineas de información. False en caso contrario.

    """
    return linecache.getline(file_name, 3) is not None


def validate_file_with_cyphers(file_name: str) -> bool:
    """
    Método auxiliar para verificar que el archivo con las
    t-partes sea válido. Esto es, que no haya sido alterado
    posterior al proceso de encriptación.

    Parámetros
    ----------
        file_name - Ruta del archivo a validar.

    Regresa
    -------
        bool - True en caso de ser un archivo válido. False en caso contrario.
    """
    enough_lines = file_has_more_than_two_lines(file_name)
    pair_number_of_lines = True
    only_numbers = True
    line_counter = 0

    with open(file_name, "r") as checking:
        for line in checking:
            line = line.split()
            for value in line:
                try:
                    int(value)
                except ValueError:
                    only_numbers = False
                    break
            line_counter += 1
    if line_counter % 2 != 0:
        pair_number_of_lines = False

    # Todos deben ser True para ser un archivo válido.
    return enough_lines == pair_number_of_lines == only_numbers


def input_validator(file_with_cyphers: str, file_to_decipher: str) -> (str, str):
    """
    Método validador del input ingresado para desencriptar un archivo.

    Parámetros
    ----------
        file_with_cyphers: str - Ruta del Archivo con las t-partes a evaluar.
        file_to_decipher: str - Ruta del Archivo a descifrar.

    Regresa
    -------
         file_with_cyphers: str - Ruta del Archivo con las t-partes a evaluar.
         file_to_decipher: str - Ruta del Archivo a descifrar.

    """

    try:
        if path.exists(file_with_cyphers) is False or path.exists(file_to_decipher) is False:
            raise shamir_exceptions.FileDoesntExistError()
        elif validate_file_with_cyphers(file_with_cyphers) is False:
            raise shamir_exceptions.NotEnoughInformationError(file_with_cyphers)
    except ValueError as error:
        print(f"{error}\n")

    print("\nArgumentos Ingresados Válidados. Iniciando Proceso de Desencriptación\n")

    return file_with_cyphers, file_to_decipher
