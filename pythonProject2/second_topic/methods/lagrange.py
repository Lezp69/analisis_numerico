import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def lagrange_basis(x_values, i, x):
    """
    Calculate the Lagrange basis polynomial Li(x).

    Parameters:
        x_values: list or array-like, x coordinates of known data points.
        i: int, index of the Lagrange basis polynomial.
        x: float, value at which to evaluate the polynomial.

    Returns:
        float, the value of the Lagrange basis polynomial Li(x) at x.
    """

    result = 1.0
    n = len(x_values)

    for j in range(n):
        if j != i:
            result *= (x - x_values[j]) / (x_values[i] - x_values[j])

    return result

def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange interpolation method.

    Parameters:
        x_values: list or array-like, x coordinates of known data points.
        y_values: list or array-like, y coordinates of known data points.
        x: float, value at which to interpolate.

    Returns:
        float, interpolated value at x.
    """

    if len(x_values) != len(y_values):
        raise ValueError("Length of x_values and y_values must be the same")

    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i] * lagrange_basis(x_values, i, x)
        result += term

    return result




