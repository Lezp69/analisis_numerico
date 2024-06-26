import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def function(x):
    return (x-2)/(x-3)

a=1
b=5
tol = 10**-6
i = 1
FA = function(a)


# while i < 30:
#     p = a + (b-a)/2
#     FP = function(p)
#     if FP == 0 or (b-a)/2 < tol:
#         print(f'La raiz es {p}')
#         break
#     i += 1
#     if FA*FP > 0:
#         a = p
#         FA = FP
#     else:
#         b = p
#
# print(f'El valor de la funcion en la raiz es {FP}')



x = np.linspace(1, 5, 1000)
y = function(x)

plt.plot(x, y, label="f(x) = (x-2)/(x-3)")


#plt.axhline(0, color='green', linewidth=1)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = (x-2)/(x-3) in [1, 5]")

plt.axvline(x=3, color='red', linestyle='dashed', linewidth=1, label='x = 3 (asíntota)')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()