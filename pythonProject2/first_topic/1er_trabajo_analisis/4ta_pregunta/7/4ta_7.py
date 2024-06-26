import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sin = np.sin

# Define the range of x values
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Calculate y values for y = x
y1 = x
# Calculate y values for y = 2sin(x)
y2 = 2 * np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y = x', color='blue')
plt.plot(x, y2, label='y = 2sin(x)', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico de y = x ^ y = 2sin(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.7)
plt.axvline(0, color='black',linewidth=0.7)
plt.show()


# Bisection


def function(x):
    return x - (2*sin(x))

tol = 10**-5
i = 1
a=1
b=3
nO=30

FA = function(a)

def bisec(a, b, FA, nO, tol, i):
    while i < nO:
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
    return print(f'Terminó el loop. El valor de p es {p} y el numero de iteraciones es {i}')

bisec(a, b, FA, nO, tol, i)
