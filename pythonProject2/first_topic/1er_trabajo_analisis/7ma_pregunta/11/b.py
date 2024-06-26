import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from math import sin, cos, e

e = np.exp(1)

#Newton method

def f(x):
    return 2*x + 3*cos(x) - e**x

def h(x):
    return 2 - 3*sin(x) - e**x

def g(x):
    return x - f(x)/h(x)

def newton(i,nO,tol,p0):
    print(f'Este es el metodo Newton')
    while i <= nO:
        p = g(p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        p0 = p
    print(f'El valor de p es {p} y el numero de iteraciones es {i}')

nO = 30
tol = 10**-5
p0 = 0.5
i = 1

newton(i,nO,tol,p0)

#Secant Method


def s(x,y):
    return x - f(x)*((x-y)/(f(x)-f(y)))

nO = 30
tol = 10**-5
i = 2

p0 = 0.25
p1 = 0.5
f0 = f(p0)
f1 = f(p1)

def secant(i,nO,tol,p0,p1,f0,f1):
    print(f'Este es el metodo Secante')
    while i <= nO:
        p = s(p1,p0)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        p0 = p1
        f0 = f1
        p1 = p
        f1 = f(p)
    print(f'El valor de p es {p} y el numero de iteraciones es {i}')

secant(i,nO,tol,p0,p1,f0,f1)