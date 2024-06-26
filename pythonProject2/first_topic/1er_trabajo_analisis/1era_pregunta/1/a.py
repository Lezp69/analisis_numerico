import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier



def truncated_sum_forward():
    sum_forward = 0
    for i in range(1, 101):
        term = truncate(1 / (i ** 2), 3)
        sum_forward += term
        print(f'En el termino {i}: {term} - Suma parcial: {sum_forward}')
    return truncate(sum_forward, 3)

def truncated_sum_backward():
    sum_backward = 0
    for i in range(100, 0, -1):
        term = truncate(1 / (i ** 2), 3)
        sum_backward += term
        print(f'Termino {i}: {term} - Suma parcial: {sum_backward}')
    return truncate(sum_backward, 3)

sum_forward = truncated_sum_forward()
print("Resultado forward:", sum_forward)

sum_backward = truncated_sum_backward()
print("Resultado backward:", sum_backward)




def truncate_float(float_number):
    float_str = str(float_number)
    non_zero_index = next((i for i, c in enumerate(float_str) if c != '0' and c != '.'), None)
    if non_zero_index is not None:
        truncated_str = float_str[:non_zero_index + 3]
        return float(truncated_str)
    else:
        return 0.0

sum_backward = 0
for i in range(100, 0, -1):
    term = truncate_float(1 / (i ** 2))
    sum_backward += term
    sum_backward = truncate(sum_forward,3)
    print(f'En el termino {i}: {term} - Suma parcial: {sum_backward}')
print("Backward Result:", sum_backward)

sum_forward = 0
for i in range(1, 101):
    term = truncate_float(1 / (i ** 2))
    sum_forward += term
    sum_forward = truncate(sum_forward,3)
    print(f'En el termino {i}: {term} - Suma parcial: {sum_forward}')
print("Forward Result:", sum_forward)