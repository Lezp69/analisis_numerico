import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def nevilles_interpolation(x_values, f_values, x):
    n = len(x_values)  # number of data points
    Q = [[0] * n for _ in range(n)]  # initialize Q table

    # Initialize first column of Q with f_values
    for i in range(n):
        Q[i][0] = f_values[i]

    # Construct the Q table using Neville's algorithm
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i][j] = ((x - x_values[i - j]) * Q[i][j - 1] - (x - x_values[i]) * Q[i - 1][j - 1]) / (x_values[i] - x_values[i - j])

    interpolated_value=Q[-1][-1]
    # Return the Q table
    return Q,interpolated_value
