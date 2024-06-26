import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from second_topic.methods.lagrange import lagrange_basis, lagrange_interpolation
# For the given functions f (x), let x0 = 0, x1 = 0.6, and x2 = 0.9.
# Construct interpolation polynomials of degree at most one and at most two to approximate
# f (0.45), and find the absolute error.


def f(x):
    return np.cos(x)

x_values = [0, 0.6, 0.9]
y_values = [f(x) for x in x_values]
x_interpolate = 0.45

interpolated_value = lagrange_interpolation(x_values, y_values, x_interpolate)
print(f"Interpolated value at x={x_interpolate}: {interpolated_value}")
print(f"Actual value at x={x_interpolate}: {f(x_interpolate)}")
print(f"Absolute error: {abs(f(x_interpolate) - interpolated_value)}")

x_range = np.linspace(0, 3, 400)
y_function = f(x_range)
y_interpolation = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

plt.plot(x_range, y_function, label='f(x) = cos(x)')
plt.scatter(x_values, y_values, color='red', label='Data Points')
plt.plot(x_range, y_interpolation, linestyle='--', label='Lagrange Interpolation')
plt.scatter(x_interpolate, interpolated_value, color='yellow', label=f'Interpolated Value at x={x_interpolate}')
plt.scatter(x_interpolate, f(x_interpolate), color='blue', label=f'({x_interpolate}, f({x_interpolate}))', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()