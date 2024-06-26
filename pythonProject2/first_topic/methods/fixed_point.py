import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fixed Point

def g(x):
    return (x**2) - 1

nO = 30
i = 1
tol = 10**-6
p0 = 0



while i < nO:
    p = g(p0)
    if abs(p-p0) < tol:
        print(f'La raiz es {p}')
        break
    i += 1
    p0 = p

print(f'El valor de p es {p} y el numero de iteraciones es {i}')