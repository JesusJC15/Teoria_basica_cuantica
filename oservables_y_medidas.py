import math
import numpy as np


def normalizar(vect):
    """Normaliza un vector
    (vect) -> vect
    """
    norm = np.linalg.norm(vect)
    if norm == 0:
        return vect
    vect_n = np.round(vect / norm, 2)
    print(norm)
    return vect_n


def part_una_linea(vect, pos):
    """Sistema probabilistico de una linea
    (vect, int) -> float
    """
    pos = vect[pos]
    pos = (np.linalg.norm(pos)) ** 2
    vect = (np.linalg.norm(vect)) ** 2
    prob = np.round(pos / vect, 2)
    return prob


def ampli_tran(vect1, vect2):
    """Calcula la probabilidad de la amplitud de transicion de un vector a otro
    (vect, vect) -> cplx
    """
    vect1 = normalizar(vect1)
    vect2 = normalizar(vect2)
    bra = np.conjugate(np.transpose(vect2))
    prod_int = np.dot(bra, vect1)
    prob = np.linalg.norm(prod_int)**2
    return np.round(prob, 0)
