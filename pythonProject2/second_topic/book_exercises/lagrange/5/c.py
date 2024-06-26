import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from second_topic.methods.lagrange import lagrange_basis, lagrange_interpolation

x_values = [0.1, 0.2, 0.3, 0.4]
y_values = [0.62049958, -0.28398668, 0.00660095, 0.24842440]

x_interpolate = 0.25

# First Degree
interpolated_values = []
for i in range(len(x_values)):
    for j in range(i + 1, len(x_values)):
        x_pair = [x_values[i], x_values[j]]
        y_pair = [y_values[i], y_values[j]]
        interpolated_value = lagrange_interpolation(x_pair, y_pair, x_interpolate)
        interpolated_values.append(interpolated_value)
        print(f"Interpolated value using {x_pair}: {interpolated_value}")

print('----------')

#Second Degree
interpolated_values = []
for i in range(len(x_values)):
    for j in range(i + 1, len(x_values)):
        for k in range(j + 1, len(x_values)):
            x_triple = [x_values[i], x_values[j], x_values[k]]
            y_triple = [y_values[i], y_values[j], y_values[k]]
            interpolated_value = lagrange_interpolation(x_triple, y_triple, x_interpolate)
            interpolated_values.append(interpolated_value)
            print(f"Interpolated value using {x_triple}: {interpolated_value}")

print('----------')

#Third Degree
interpolated_value = lagrange_interpolation(x_values, y_values, x_interpolate)
print(f"Interpolated value at x={x_interpolate}: {interpolated_value}")

print('----------')

#Using the formula in the excersice 7
def f(x):
    return x*np.cos(x) - 2*x**2 + 3*x - 1

true_y = f(x_interpolate)
print(f"Actual value at x={x_interpolate}: {true_y}")

#Graphic
x_range = np.linspace(0, 1, 400)
y_function = f(x_range)
y_interpolation = [lagrange_interpolation(x_values, y_values, x) for x in x_range]

plt.plot(x_range, y_function, label='f(x) = xcos(x) − 2x^2 + 3x − 1')
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