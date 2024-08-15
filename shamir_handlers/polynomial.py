"""
Archivo con los métodos del polinomio de interpolación y la evaluación del polinomio

Autor: @TheSinotec
Version: 1.1
"""

# Libreria para cálculo numérico y manejo de Arrays
import numpy as np
# Libreria para el cálculo simbólico de fracciones (problema de precisión en interpolación con enteros enormes)
import fractions
# Libreria de tiempo de la máquina
import datetime
from hashlib import sha256


def auxiliar_function(a: fractions.Fraction, b: fractions.Fraction, c: fractions.Fraction, d: fractions.Fraction):
    """
    Método auxiliar para el cálculo de los coeficientes de la interpolación de Newton

   Parámetros:
   -----------
        a - fractions.Fraction. Valor a (x).
        b - fractions.Fraction. Valor b (x).
        c - fractions.Fraction. Valor c (y).
        d - fractions.Fraction. Valor d (y).

    Regresa:
    --------
        Fraction((d - c) / (b - a)) - fractions.Fraction. Cociente simbólico de tipo Fraction
        (operación marcada por la salida).
    """
    return fractions.Fraction((d - c) / (b - a))


def evaluate(x: int, t: int, coefficients: np.array):
    """
    Método auxiliar para evaluar en un punto un polinomio p(x) de grado t-1 con coeficientes coefficients[i]; p(0) = 0
    
   Parámetros:
   -----------
        x - int. Valor x a evaluar en p(x).
        t - int. Grado del polinomio (t-1).
        coefficients - np.array. Arreglo con los coeficientes asociados a cada potencia del polinomio.

    Regresa:
    --------
        sumatory - fractions.Fraction. Evaluación del polinomio p(x) en fracción simbólica.
    """
    sumatory = fractions.Fraction(0)
    for i in range(1, t):
        pow_part = x ** i
        term = fractions.Fraction(pow_part) * coefficients[i - 1]
        sumatory = sumatory + term
    return sumatory


def gen_keys(divisions: int, min_parts: int, file_name: str, key: int):
    """
    Método generador del archivo *.frg con los n fragmentos, para al menos t llaves necesarias. p(0) = key
    
   Parámetros:
   -----------
        divisions - int. Cantidad de llaves (o fragmentos) generados en el archivo *.frg.
        min_parts - int. Cantidad de llaves (o fragmentos) mínimos para recuperar la key (password).
        file_name - str. Nombre del archivo a generarse, es decir file_name.frg.
        key - int. Arreglo de bytes convertido a entero, asociado a la contraseña.

    Regresa:
    --------
        Genera un archivo de nombre file_name de extensión *.frg, no regresa parámetros.
    """
    np.random.seed(int(datetime.datetime.now().microsecond))
    coefficients = np.random.choice([p for p in range(-divisions, divisions) if p not in [0]], min_parts - 1)
    file = open(file_name + '.frg', 'w')
    no_repeat_x = []
    x = np.random.randint(1, 2 * divisions)
    for z in range(divisions):
        while x in no_repeat_x:
            x = np.random.randint(1, 2 * divisions)
        no_repeat_x.append(x)
        file.writelines([str(x) + " " + str(int(evaluate(x, min_parts, coefficients)) + key) + "\n"])


def from_keys(file_name: str):
    """
    Método del polinomio de interpolación de Newton para la obtención de un arreglo de bytes asociado a p(0) = key
    de un polinomio de n evaluaciones para un archivo *.frg
    
   Parámetros:
   -----------
        file_name - str. Nombre del archivo de *.frg, es decir file_name.frg, para el cuál se interpolan
                    sus puntos contenidos.

    Regresa:
    --------
        intercept_key - bytes. Arreglo de bytes asociado a la ordenada al origen del polinomio de interpolación.
        failed_key - bytes. Arreglo de bytes aleatorio asociado a la ordenada al origen que excede las
                            características esperadas por el polinomio de interpolación.
    """
    with open(file_name, 'r') as file:
        data = file.read().split()
        x = []
        y = []
        zeros = [0] * (int(len(data) / 2) - 1)
        for i in range(int(len(data) / 2)):
            x.append(int(data[2 * i]))
            auxiliar_y = zeros.copy()
            auxiliar_y.insert(0, fractions.Fraction(int(data[2 * i + 1])))
            y.append(auxiliar_y)
    for j in range(1, len(x)):
        for i in range(len(x) - j):
            y[i][j] = auxiliar_function(fractions.Fraction(x[i + j]), fractions.Fraction(x[i]), fractions.Fraction(y[i + 1][j - 1]), fractions.Fraction(y[i][j - 1]))
    sumatory = y[0][0]
    for i in range(1, int(len(data) / 2)):
        product = 1
        for j in range(i):
            product = product * (-x[j])
        product = product * y[0][i]
        sumatory = sumatory + product
    reconstruct = int(sumatory)
    try:
        intercept_key = reconstruct.to_bytes(32, 'little')
        return intercept_key
    except OverflowError:
        abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&()*+,-.:;<=>?@[]^_`{|}~"
        failed_key = ""
        for i in np.random.choice(list(abc), 7):
            failed_key = failed_key + i
        failed_key = failed_key.encode('utf-8')
        failed_key = sha256(failed_key).digest()
        return failed_key
