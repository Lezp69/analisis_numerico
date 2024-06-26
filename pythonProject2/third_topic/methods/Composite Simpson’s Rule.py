import numpy as np
import matplotlib.pyplot as plt
import math


def composite_simpsons_rule(f, a, b, n):
    # Step 1: Set h
    h = (b - a) / n

    # Step 2: Initialize XI0, XI1, XI2
    XI0 = f(a) + f(b)
    XI1 = 0  # Summation of f(x2i−1)
    XI2 = 0  # Summation of f(x2i)

    # Step 3: Loop from 1 to n-1
    for i in range(1, n):
        # Step 4: Set X
        X = a + i * h

        # Step 5: Update XI1 and XI2 based on whether i is even or odd
        if i % 2 == 0:
            XI2 += f(X)
        else:
            XI1 += f(X)

    # Step 6: Calculate XI
    XI = h * (XI0 + 2 * XI2 + 4 * XI1) / 3

    print(f'XI: {XI}')

    # Step 7: Output XI
    return XI

# Example (not in code)

# Define the function to integrate
#def f(x):
    #return x**2
# Define the interval [a, b] and the number of subintervals n (must be even)
#a = 0
#b = 1
#n = 10

# Call the composite_simpsons_rule function
#result = composite_simpsons_rule(f, a, b, n)