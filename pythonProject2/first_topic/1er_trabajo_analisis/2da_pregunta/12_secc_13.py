import pandas as pd
import numpy as np

x = 0.25
print(f'x={x}')

ld = (1+(2*x))/(1+x+(x**2))
print(f'ld={ld}')


def second_x_exponent_up(i):
    sequence = [0]
    for _ in range(i):
        next_term = 2 * sequence[-1] + 1
        sequence.append(next_term)
    return sequence[-1]


def first_x_exponent_up(i):
    sequence = [0]
    for j in range(1, i + 1):
        next_term = sequence[-1] + j
        sequence.append(next_term)
    return sequence[-2]

print(f'second_x_exponent_up:{second_x_exponent_up(3)}')  # Output should be 7
print(f'first_x_exponent_up:{first_x_exponent_up(3)}')  # Output should be 3

i = 1

def progression(i):
    a = (((2**(i-1))*(x**first_x_exponent_up(i))) - ((2**i) * (x**second_x_exponent_up(i))))/(1-x**(2**(i-1))+x**(2**i))
    return a

li = progression(i)

print(f'li={li} y ld={ld}')

tol = 10**-6

while abs(li-ld) >= tol:
    print(f'li en la iteracion {i} es {li}')
    i+=1
    li = li + progression(i)
    print(li)
