"""
Métodos para encriptar y desencriptar usando AES

Author: @Santi24Yt
Version: 1.1
"""

# Librería actualizada con métodos de encriptación
from Crypto.Cipher import AES


def encrypt(key, data):
    """Encripta los datos con una llave.

    Encripta los datos con una llave, la llave son bytes
    y los datos son un bytearray, devuelve una tupla de 2 con un iv
    (16 bytes)y los datos encriptados (bytearray),
    el iv y la llave son necesarios para desencriptar
    los datos

    Parámetros
    ----------
    key -  bytes. La llave para encriptar los datos (32 bytes)

    data - bytearray. Un bytearray con los datos a encriptar

    Regresa
    -------
    iv, encrypted - bytes, bytearray. Los bytes a poner en el archivo encriptado
    """
    aes = AES.new(key, AES.MODE_CFB)
    iv = aes.iv

    encrypted = []

    for chunk in data:
        encrypted.append(aes.encrypt(chunk))

    return iv, encrypted


def decrypt(key, iv, encrypted):
    """Desencripta los datos con una llave

    Desencripta los datos con una llave, los datos
    deben ser el iv (primeros 16 bytes),
    y los datos (un bytearray con el resto).
    Lo ideal sería obtener todo del mismo archivo.

    Parámetros
    ----------
    key - bytes. La llave que se usó para encriptar los datos (32 bytes)

    iv - bytes. El iv (16 bytes)

    encrypted - byte array. Los datos encriptados

    Regresa
    -------
    data -  bytearray. Los datos desencriptados con esa clave
    """
    aes = AES.new(key, AES.MODE_CFB, iv=iv)

    data = []
    for chunk in encrypted:
        data.append(aes.decrypt(chunk))

    return data
