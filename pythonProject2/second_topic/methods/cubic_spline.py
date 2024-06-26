import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
def natural_cubic_spline(x_values, f_values):
    n = len(x_values)
    h = [x_values[i + 1] - x_values[i] for i in range(n - 1)]

    # Check if lengths are compatible
    if len(f_values) != n:
        raise ValueError("Length of f_values should be equal to the number of x_values.")

    # Step 2
    alpha = [3 * ((f_values[i + 1] - f_values[i]) / h[i] - (f_values[i] - f_values[i - 1]) / h[i-1]) for i in range(1, n - 1)]

    # Steps 3-5 (remaining code unchanged)
    l = [0] * n
    mu = [0] * n
    z = [0] * n
    c = [0] * n
    b = [0] * n
    d = [0] * n

    # Step 3: Set l0 = 1; μ0 = 0; z0 = 0
    l[0] = 1

    # Steps 4 and 5
    for i in range(1, n - 1):
        l[i] = 2 * (x_values[i + 1] - x_values[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (3 * ((f_values[i + 1] - f_values[i]) / h[i] - (f_values[i] - f_values[i - 1]) / h[i - 1])) / l[i]

    l[n - 1] = 1  # Step 5
    z[n - 1] = 0  # Step 5

    # Step 6
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (f_values[j + 1] - f_values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    # Prepare output
    coefficients = [(f_values[i], b[i], c[i], d[i]) for i in range(n - 1)]
    for j, coeff in enumerate(coefficients):
        print(f"Interval {j + 1}: a={coeff[0]}, b={coeff[1]}, c={coeff[2]}, d={coeff[3]}")
    return coefficients

def evaluate_spline(coefficients, x_values, x):
    for i, (a, b, c, d) in enumerate(coefficients):
        if x_values[i] <= x <= x_values[i + 1]:
            dx = x - x_values[i]
            return a + b * dx + c * dx**2 + d * dx**3
    raise ValueError("x is outside the range of x_values")
