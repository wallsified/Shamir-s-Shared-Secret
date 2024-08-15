"""
Archivo para el proceso del Secreto
Compartido de Shamir.

Author: @wallsified
Version: 1.0
"""

import argparse
import sys

from shamir_decrypt.decrypt_process import initiate_decrypt_process
from shamir_encrypt.encrypt_process import initiate_encrypt_process

# Limitamos a que solo se vean los mensajes de error personalizados
sys.tracebacklimit = 5


def parse_args():
    """
    Método para pasar argumentos a la llamada del script.
    """

    description = "Script para cifrar un archivo usando el Secreto Compartido de Shamir."
    parser = argparse.ArgumentParser(description=description, prog="Secreto Compartido de Shamir",
                                     epilog="¡Gracias por usar nuestro programa!")
    parser.add_argument("--mode", help="Modo de Ejecución. Usa 'C/c' para cifrar y 'D/d' para descifrar",
                        type=str, required=True)
    parser.add_argument("--file", help="Archivo a Cifrar o Descifrar", type=str, required=False)
    parser.add_argument("--name", help="Nombre del Archivo Encriptado", type=str, required=False)
    parser.add_argument("--divisions", help="Cantidad de Divisiones para el Archivo", type=int)
    parser.add_argument("--min", help="Cantidad mínima de partes para descifrar", type=int)
    parser.add_argument("--cyphered", help="Archivo con la información para descifrar", type=str)

    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    argue = parse_args()
    if argue.mode.lower() == "c":
        initiate_encrypt_process(argue.file, argue.name, argue.divisions, argue.min)
    if argue.mode.lower() == "d":
        initiate_decrypt_process(argue.file, argue.cyphered)
