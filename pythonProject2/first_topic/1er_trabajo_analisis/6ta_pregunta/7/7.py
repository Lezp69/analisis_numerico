import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fixed Point
def fixed_point(p0, tol, nO, i):
    values_of_p = []
    while i <= nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        values_of_p.append(p)
        if abs(p - p0) < tol:
            print(f'La raiz es {p}')
            return p, values_of_p
        i += 1
        p0 = p
    print(f'Terminó el loop. El valor de p es {p} y el numero de iteraciones es {i}')
    return p, values_of_p

nO = 10
tol = 10**-2
i = 1
p0 = 1

def g(x):
    return np.pi+ 0.5*np.sin(x/2)

root, values = fixed_point(p0, tol, nO, i)
print(f'Valores de P con un maximo de numero de iteraciones de {nO}:, {values}')