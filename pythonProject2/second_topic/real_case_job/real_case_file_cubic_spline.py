import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import re
import tabula
from tabula import read_pdf
from second_topic.methods.cubic_spline import natural_cubic_spline, evaluate_spline
from second_topic.methods.divided_differences import interpolate_newtons_divided_difference
from second_topic.methods.lagrange import lagrange_basis, lagrange_interpolation
from second_topic.methods.neville import nevilles_interpolation


excel_path = r"C:\Users\luisz\Downloads\research-2015-smoker-distinct-loaded-cso.xlsx"

# Specify the sheet name or index you want to read (e.g., sheet_name='Sheet1' or sheet_name=0)
sheet_name = '2017 MSM ANB'  # Replace 'YourSheetName' with the actual sheet name or index

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path, sheet_name=sheet_name, header=1)
# Reset the index after dropping rows (optional)
df = df.reset_index(drop=True)
print(df)

df.columns = df.iloc[0]
df = df[1:]
print(df)

# Extract the columns of interest
x_values = df['Iss. Age'].tolist()
y_values = df[1.0].tolist()
print(x_values)
print(y_values)


#Divided Differences
coefficients = natural_cubic_spline(x_values, y_values)
print(f'Cubic Spline Coefficients: {coefficients}')
# Plotting
x_range = np.linspace(min(x_values), max(x_values), 100)
y_interp = [evaluate_spline(coefficients, x_values, x) for x in x_range]


plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, label='Original Data', color='blue')
plt.plot(x_range, y_interp, label='Divided Differences Interpolation', color='red')
plt.xlabel('Iss. Age')
plt.ylabel('Value')
plt.title('Divided Differences Interpolation')
plt.legend()
plt.grid(True)
plt.ylim(min(y_values) - 1, max(y_values) + 1)
plt.show()