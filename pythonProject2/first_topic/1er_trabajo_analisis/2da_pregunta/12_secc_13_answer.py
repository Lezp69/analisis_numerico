import pandas as pd
import numpy as np

x = 0.25
print(f'x={x}')

ld = (1+(2*x))/(1+x+(x**2))
print(f'ld={ld}')

i = 0
tol = 10**-6

def progression(i):
    a=((2**i)*x**((2**i)-1)-(2**(i+1))*x**((2**(i+1))-1))/(1-x**(2**i)+x**(2**(i+1)))
    return a

li = progression(i)

while abs(li-ld) >= tol:
    print(f'li en la iteracion {i} es {li}')
    i+=1
    li = li + progression(i)
    print(li)