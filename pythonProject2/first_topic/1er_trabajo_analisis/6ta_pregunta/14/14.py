import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fixed Point
def fixed_point(p0, tol, nO,i):
    while i <= nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            return p
        i += 1
        p0 = p
    return print(f'Terminó el loop. El valor de p es {p} y el numero de iteraciones es {i}')
nO = 30
tol = 10**-4
i = 1
p0 = 4.5

def g(x):
    return np.tan(x)

fixed_point(p0, tol, nO,i)