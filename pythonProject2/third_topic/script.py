import numpy as np
import matplotlib.pyplot as plt
import math
from methods.trapezoidal import trapezoidal

x_base = [0, 2]
# Define the x values for the sine function
x_sine = np.linspace(0, 2, 100)  # Generate 100 points between 0 and 2
# Calculate the y values for the sine function
y_sine = np.sin(x_sine)
# Calculate the y values for the trapezoid
y_trapezoid = [np.sin(x_base[0]), np.sin(x_base[1])]
# Define the vertices of the trapezoid
vertices = [(x_base[0], np.sin(x_base[0])), (x_base[1], np.sin(x_base[1]))]
# Plot the trapezoid base
plt.plot(x_base, y_trapezoid, 'r-', label='Trapezoid')
# Plot the lines extending from y-values to the corresponding x-values
for vertex in vertices:
    print(vertex)
    print([vertex[0], vertex[0]], [0, vertex[1]])
    plt.plot([vertex[0], vertex[0]], [0, vertex[1]], 'g--')
# Plot the sine function
plt.plot(x_sine, y_sine, 'b-', label='sin(x)')
# Label the axes
plt.xlabel('x')
plt.ylabel('y')
# Add a legend
plt.legend()
# Show the plot
plt.show()

print(trapezoidal(x_base[0], x_base[1], y_trapezoid[0], y_trapezoid[1]))