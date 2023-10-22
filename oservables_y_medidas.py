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
    """Sistema probabilístico de una línea
    (vect, int) -> float
    """
    prob = np.round(np.abs(vect[pos])**2, 2)
    return prob

def ampli_tran(vect1, vect2):
    """Calcula la probabilidad de la amplitud de transición de un vector a otro
    (vect1, vect2) -> float
    """
    vect1 = normalizar(vect1)
    vect2 = normalizar(vect2)
    bra = np.conjugate(np.transpose(vect2))
    prod_int = np.dot(bra, vect1)
    prob = np.round(np.abs(prod_int)**2, 2)
    return prob

def media_varianza(mat_obs, vect_est):
    """Calcula la media y la varianza del observable en el estado dado.
    (mat_obs, vect_est) -> (float, float)
    """
    val_esp = np.real(np.dot(vect_est.conj().T, np.dot(mat_obs, vect_est)))
    mat_obs_cua = np.dot(mat_obs, mat_obs)
    val_esp_cua = np.real(np.dot(vect_est.conj().T, np.dot(mat_obs_cua, vect_est)))
    vari = val_esp_cua - val_esp**2
    return val_esp, vari

def val_y_vect_prop(mat_obs, vect_est):
    """Calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
    (mat_obs, vect_est) -> (np.ndarray, np.ndarray)
    """
    val_pro, vect_pro = np.linalg.eig(mat_obs)
    proba = np.abs(np.dot(vect_pro.conj().T, vect_est)) ** 2
    return val_pro, proba
