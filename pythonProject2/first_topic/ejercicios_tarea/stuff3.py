import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def function(x):
    return (x**2) + 1

a=-1
b=1
tol = (10**-6)
i = 1
FA = function(a)


while i < 30:
    p = a + (b-a)/2
    FP = function(p)
    if FP == 0 or (b-a)/2 < tol:
        print(f'La raiz es {p}')
        break
    i += 1
    if FA*FP > 0:
        a = p
        FA = FP
    else:
        b = p

print(f'El valor de la funcion en la raiz es {FP} y el numero de iteraciones es {i}')
print(f'El valor de a es {a} y el valor de b es {b}')


x = np.linspace(-1, 1, 1000)
y = function(x)

plt.plot(x, y, label="f(x) = x^2 + 1")


plt.axhline(0, color='red', linewidth=1)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = x^2 + 1 in [-1, 1]")


# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()