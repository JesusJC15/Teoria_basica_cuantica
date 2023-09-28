import numpy as np
import math


def normalizar(vect):
    """Normaliza un vector
    (vect) -> vect
    """
    norm = np.linalg.norm(vect)
    if norm == 0:
        return vect
    vect_n = np.round(vect / norm, 2)
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


def transitar(vect1, vect2):
    """Calcula la amplitud de transicion de un vector a otro
    (vect, vect) -> cplx
    """
    vect1 = normalizar(vect1)
    vect2 = normalizar(vect2)
    bra = np.conjugate(np.transpose(vect2))
    prod_int = np.dot(bra, vect1)
    return np.round(prod_int, 0)