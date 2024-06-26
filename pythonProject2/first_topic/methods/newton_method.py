import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# newton method
def f(x):
    return x**2

def h(x):
    return 2*x

def g(x):
    return x - f(x)/h(x)

nO = 30
tol = 10**-6
p0 = 1
i = 1

def newton_method(p0, nO, tol,i):
    while i < nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        p0 = p
    print(f'El valor de p es {p} y el numero de iteraciones es {i}')
