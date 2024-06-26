import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bisection

def function(x):
    return (x**2) - 1

a=-2
b=2
tol = 10**-6
i = 1
FA = function(a)


while i < 30:
    p = a + (b-a)/2
    print(f'El valor de p en la iteracion {i} es {p}')
    FP = function(p)
    print(f'El valor de FP en la iteracion {i} es {FP}')
    if FP == 0 or ((b-a)/2) < tol:
        print(f'La raiz es {p}')
        break
    i += 1
    if FA*FP > 0:
        a = p
        FA = FP
    else:
        b = p

print(f'El valor de p es {p} y el numero de iteraciones es {i}')