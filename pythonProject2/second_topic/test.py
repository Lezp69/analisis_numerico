import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from second_topic.methods.cubic_spline import natural_cubic_spline

# Example usage (updated to include sufficient f_values):
x_values = [0,1,2,3]  # x values
f_values = [1,math.exp(1),math.exp(2),math.exp(3)]  # f(x) values (must be equal to the number of x_values)
coefficients = natural_cubic_spline(x_values, f_values)

def evaluate_spline(coefficients, x_values, x):
    for i, (a, b, c, d) in enumerate(coefficients):
        if x_values[i] <= x <= x_values[i + 1]:
            dx = x - x_values[i]
            return a + b * dx + c * dx**2 + d * dx**3
    raise ValueError("x is outside the range of x_values")


x_plot = np.linspace(min(x_values), max(x_values), 1000)
y_plot = [evaluate_spline(coefficients, x_values, x) for x in x_plot]

y_plot_exponential = np.exp(x_plot)  # True values of f(x) = exp(x)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, f_values, 'ro', label='Data Points')  # Plot the original data points
plt.plot(x_plot, y_plot, label='Cubic Spline')  # Plot the cubic spline curve
plt.plot(x_plot, y_plot_exponential, label='e^x')  # Plot e^x
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Natural Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()