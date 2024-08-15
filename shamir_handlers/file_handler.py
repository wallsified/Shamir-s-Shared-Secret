"""
Métodos para leer y escribir archivos

Author: @EdgarMontelongo
Version 1.1
"""

chunk_size = 16 * 1024  # 16 kB


def read_file(path):
    """
    Función de lectura de un archivo

    Parameters:
        path: el nombre del archivo a leer
    
    Returns:
        data: un arreglo de bytes 
    """
    data = []
    f = open(path, mode="rb")

    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        data.append(chunk)

    f.close()

    return data


def read_encrypted_file(path):
    """
    Función de lectura de un archivo encriptado

    Parámetros
    ----------
        path - El nombre del archivo a leer
    
    Regresa
    -------
        iv - El iv de la encriptación
        data - Un arreglo de bytes
    """
    data = []
    f = open(path, mode="rb")
    iv = f.read(16)

    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        data.append(chunk)
    f.close()

    return iv, data


def save_file(path, data):
    """
    Función de escritura de un bytearray en forma de un archivo de texto plano

    Parámetros
    ----------
        path - Nombre del archivo a escribir
        data - bytearray a escribir en el archivo

    """
    with open(path, mode='wb') as file:
        for chunk in data:
            file.write(chunk)
