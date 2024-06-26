import pandas as pd
import numpy as np

x = 0.25
print(f'x={x}')
li = (1-(2*x))/(1-x+x**2)
print(f'li={li}')

ld = (1+(2*x))/(1+x+(x**2))
print(f'ld={ld}')

i = 1

#print((2*i*x**((2*i)-1)-4*i*x**((4*i)-1))/(1-x**(2*i)+x**(4*i)))

#print(li + (2*i*x**((2*i)-1)-4*i*x**((4*i)-1))/(1-x**(2*i)+x**(4*i)))


# if abs(li-ld) > 10**6:
#     while abs(li-ld) > 10**6:
#         li = li + (2*i*x**((2*i)-1)-4*i*x**((4*i)-1))/(1-x**(2*i)+x**(4*i))
#         print(f'Numero de iteraciones {i} y el valor de la serie es {li}')
#         i += 1
# else:
#     print(f'La diferencia inicial de li-ld es: {abs(li-ld)}, y eso es menos de 10^6, por lo que no se ejecuta el ciclo while')
