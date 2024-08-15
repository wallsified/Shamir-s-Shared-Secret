"""
Método para inicializar el proceso de encriptación

Author: @wallsified, @TheSinotec
Version: 1.1
"""

from shamir_encrypt import input_validator
from shamir_handlers.crypt_decrypt import encrypt
from shamir_handlers.polynomial import gen_keys
from shamir_handlers.file_handler import read_file, save_file
import os


def initiate_encrypt_process(filename: str, output_name: str, divisions: int, minimum: int):
    """
    Método para inicializar el proceso de encriptación.
    Toma los parámetros de la terminal e inicia las
    etapas correspondientes del proceso.

    Parámetros
    ----------
        filename - str. Nombre(Ruta) del archivo a encriptar.
        output_name - str. Nombre de salida del programa.
        divisions - int. Cantidad de divisiones para la contraseña.
        minimum - int. Cantidad minima de divisiones para recuperar la contraseña.

    """
    input_path, file_name, divisions, min_parts, password = input_validator.validate_input(filename, output_name, divisions, minimum)
    key = int.from_bytes(password, byteorder='little')
    gen_keys(divisions, min_parts, file_name, key)
    data_to_encrypt = read_file(input_path)
    iv, data_encrypted = encrypt(password, data_to_encrypt)
    encrypted_file_data = [iv] + data_encrypted
    save_file(input_path+".aes", encrypted_file_data)

    print(f"El archivo {input_path} fue encriptado.\n")
