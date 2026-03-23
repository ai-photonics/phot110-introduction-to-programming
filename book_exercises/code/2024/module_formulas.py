import numpy as np


def gaussian(x, sigma):
    g = 1/np.sqrt(2*np.pi*sigma**2) * np.exp(- x ** 2 / (2 * sigma))
    return g
