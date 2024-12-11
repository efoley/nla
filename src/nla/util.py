import numpy as np


def complex_grid(real_range, imag_range, num_real, num_imag):
    re = np.linspace(*real_range, num_real)
    im = np.linspace(*imag_range, num_imag)
    zr, zi = np.meshgrid(re, im)
    return zr + 1j * zi 