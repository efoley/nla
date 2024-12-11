import numpy as np


def random_tridiagonal(n: int, gen: np.random.Generator) -> np.array:
    L = np.diag(gen.standard_normal(n-1), k=-1)
    U = np.diag(gen.standard_normal(n-1), k=1)
    D = np.diag(gen.standard_normal(n), k=0)

    return L + U + D
