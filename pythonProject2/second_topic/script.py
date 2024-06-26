import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from second_topic.methods.cubic_spline import natural_cubic_spline
from tabula import read_pdf

url = 'https://www.unitec.edu/innovare/published/volume-5/number-2/5210-interpolacion-de-splines-cubicos-para-estimaciones-en-elaboracion-de-tablas-de-mortalidad-para-honduras.pdf'
df = read_pdf(url, pages='10')
print(df[0])
df = df[0]
df = pd.DataFrame(df)
print(df)

edad_cols = [col for col in df.columns if col.startswith('Edad')]
x_values = [value for col in edad_cols for value in df[col]]
print(x_values)
fallecimientos_cols = [col for col in df.columns if col.startswith('Fallecimientos')]
f_values = [value for col in fallecimientos_cols for value in df[col]]
print(f_values)

def convert_and_clean_list(data_list):
  """
  This function takes a list of strings and returns a new list with integers.

  Args:
      data_list: A list of strings, possibly containing commas.

  Returns:
      A new list of integers.
  """
  # List comprehension to remove commas and convert to integers
  return [int(item.replace(",", "")) for item in data_list]


f_values = convert_and_clean_list(f_values)
print(f_values)

coefficients = natural_cubic_spline(x_values, f_values)
def evaluate_spline(coefficients, x_values, x):
    for i, (a, b, c, d) in enumerate(coefficients):
        if x_values[i] <= x <= x_values[i + 1]:
            dx = x - x_values[i]
            return a + b * dx + c * dx**2 + d * dx**3
    raise ValueError("x is outside the range of x_values")


x_plot = np.linspace(min(x_values), max(x_values), 50)
y_plot = [evaluate_spline(coefficients, x_values, x) for x in x_plot]


# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_values, f_values, 'ro', label='Data Points')  # Plot the original data points
plt.plot(x_plot, y_plot, label='Cubic Spline')  # Plot the cubic spline curve
plt.xlabel('Edades')
plt.ylabel('Fallecimientos')
plt.title('Natural Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()