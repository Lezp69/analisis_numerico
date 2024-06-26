import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from math import sin, cos
# secant method


def f(x):
    return -x**3-cos(x)

def g(x,y):
    return x - f(x)*((x-y)/(f(x)-f(y)))

nO = 3
tol = 10**-6
i = 2

p0 = -1
p1 = 0
f0 = f(p0)
f1 = f(p1)

while i < nO:
    p = g(p1,p0)
    print(f'El valor de p en la iteracion {i} es {p}')
    if abs(p-p0) < tol:
        print(f'La raiz es {p}')
        break
    i += 1
    p0 = p1
    f0 = f1
    p1 = p
    f1 = f(p)