import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x**3)-x-1

tol = 10**-4
i = 1
a=1
b=2
nO=13

FA = function(a)

def bisec(a, b, FA, nO, tol, i):
    p_values = []
    while i < nO:
        p = a + (b - a) / 2
        print(f'El valor de p en la iteracion {i} es {p}')
        FP = function(p)
        print(f'El valor de FP en la iteracion {i} es {FP}')
        p_values.append(p)
        if FP == 0 or ((b - a) / 2) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print(f'Terminó el loop. El valor de p es {p} y el numero de iteraciones es {i}')
    return p_values

p_values = bisec(a, b, FA, nO, tol, i)
print("Valores de P:", p_values)