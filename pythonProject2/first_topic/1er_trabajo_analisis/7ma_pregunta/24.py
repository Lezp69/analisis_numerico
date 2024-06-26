import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import  exp

# newton method
def f(x):
    return 1000000*(exp(x)) + ((435000)/(x))*((exp(x))-1) - 1564000

def h(x):
    return 1000000*(exp(x)) + ((435000*((exp(x))*x - exp(x) + 1))/(x**2))


def g(x):
    return x - f(x)/h(x)

nO = 30
tol = 10**-4
p0 = 0.5
i = 1
p =0
def newton(p0, tol, nO,i):
    while i < nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        p0 = p
    print(f'El valor de p es {p} y el numero de iteraciones es {i}')
    return p

newton(p0, tol, nO,i)

print('Finding population at the end of the second year')
print('Populaation year 2: ')
print(1564000*(exp(0.1009979296876602)) + ((435000)/(0.1009979296876602))*((exp(0.1009979296876602))-1))