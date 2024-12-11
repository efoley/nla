import numpy as np


def companion_matrix(coeffs):
    """
    Return companion matrix for the (m-1) coefficients of a monic degree m polynomial.

    This matrix will have as eigenvalues the roots of the polynomial.

    Args:
        coeffs: array of (m-1) coefficients of the polynomial ordered from lowest to
            highest degree; i.e. the coefficient of z^(m-1) is last
    """
    n = len(coeffs)
    A = np.diag(np.ones(n-1), k=-1)
    A[:, -1] = -np.array(coeffs)
    return A