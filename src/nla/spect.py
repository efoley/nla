import numpy as np


def spectral_radius(matrix: np.array):
    ew = np.linalg.eig(matrix).eigenvalues

    return np.max(np.abs(ew))


def spectral_abscissa(matrix: np.array):
    ew = np.linalg.eig(matrix).eigenvalues

    return np.max(np.real(ew))