import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def newtons_divided_difference(x_values, f_values):
    n = len(x_values)  # number of data points
    F = [[0] * n for _ in range(n)]  # initialize F table

    # Initialize first column of F with f_values
    for i in range(n):
        F[i][0] = f_values[i]

    # Construct the F table using Newton's divided difference formula
    for i in range(1, n):
        for j in range(1, i + 1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (x_values[i] - x_values[i - j])

    # Extract the diagonal elements of F for Pn(x) coefficients
    coefficients = [F[i][i] for i in range(n)]

    # Return the coefficients for Pn(x) = F0,0 + Σ Fi,i * ∏(x - xj) from i=1 to n
    return coefficients

def interpolate_newtons_divided_difference(x_values, f_values, x):
    coefficients = newtons_divided_difference(x_values, f_values)
    n = len(coefficients)
    result = coefficients[0]  # Initialize with F0,0

    for i in range(1, n):
        term = coefficients[i]  # Fi,i
        for j in range(i):
            term *= (x - x_values[j])  # ∏(x - xj)
        result += term  # Add to the result

    return result