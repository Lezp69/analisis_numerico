import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fixed Point
def fixed_point(p0, tol, nO,i, limit):
    while i <= nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol or abs(p-limit) < tol:
            print(f'La raiz es {p}')
            return p
        i += 1
        p0 = p
    return print(f'Terminó el loop. El valor de p es {p} y el numero de iteraciones es {i}')
limit = 21**(1/3)
nO = 100
tol = 10**-6



#a
i = 1
p0 = 1

def g(x):
    return ((20*x)+(21/x**2))/21

fixed_point(p0, tol, nO,i, limit)

#b
print(f'Esto es para la pregunta b')
i = 1
p0 = 1
def g(x):
    return x - (x**3 - 21)/(3*x**2)

fixed_point(p0, tol, nO,i, limit)

#c
print(f'Esto es para la pregunta c')
i = 1
p0 = 1
def g(x):
    return x - (x**4 - 21*x)/(x**2 - 21)

fixed_point(p0, tol, nO,i, limit)

#d
print(f'Esto es para la pregunta d')
i = 1
p0 = 1
def g(x):
    return (21/x)**(1/2)

fixed_point(p0, tol, nO,i, limit)