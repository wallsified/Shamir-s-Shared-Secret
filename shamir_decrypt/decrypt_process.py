"""
Método para inicializar el proceso de desencriptación

Author: @wallsified, @TheSinotec
Version: 1.1
"""
import os

from shamir_decrypt.input_validator import input_validator
from shamir_handlers.crypt_decrypt import decrypt
from shamir_handlers.polynomial import from_keys
from shamir_handlers.file_handler import save_file
from shamir_handlers.file_handler import read_encrypted_file


def initiate_decrypt_process(file_name: str, key_file_name: str):
    """
    Método para inicializar el proceso de desencriptación.
    Toma los parámetros de la terminal e inicia las
    etapas correspondientes del proceso.

    Parámetros
    ----------
        file_name - Nombre(Ruta) del archivo a desencriptar.
        key_file_name - Nombre/Ruta del archivo con las partes a descifrar la contraseña.

    """
    file_to_decipher, file_with_cyphers = input_validator(file_name, key_file_name)
    password_bytes = from_keys(file_with_cyphers)
    iv, encrypted_file_data = read_encrypted_file(file_to_decipher)
    decrypt_bytes = decrypt(password_bytes, iv, encrypted_file_data)
    save_file(file_to_decipher[:-4]+".decrypt", decrypt_bytes)
    print(f"El archivo {file_to_decipher} fue desencriptado.\n")
