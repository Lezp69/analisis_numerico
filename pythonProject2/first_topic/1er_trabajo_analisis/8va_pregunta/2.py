import math


def f(x):
    return math.exp(6*x) + 3 * (math.log(2))**2 * math.exp(2*x) - (math.log(8)) * math.exp(4*x) - (math.log(2))**3

print(f'f(0) = {f(0)}')
def h(x):
    return 6*math.exp(6*x) + 6 * (math.log(2))**2 * math.exp(2*x) - 4*(math.log(8))*math.exp(4*x)

print(f'h(0) = {h(0)}')

def g(x):
    return x - f(x)/h(x)

print(f'g(0) = {g(0)}')

nO = 30
tol = 0.0002
p0 = 0
i = 1



def newton_method(p0, nO, tol,i):
    p_values = []
    while i < nO:
        p = g(p0)
        p_values.append(p)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-p0) < tol:
            print(f'La raiz es {p}')
            break
        i += 1
        p0 = p
    print(f'Usando el metodo de Newton. El valor de p es {p} y el numero de iteraciones es {i}')
    return p, p_values[:3]

final_approximation, first_three_values = newton_method(p0, nO, tol, i)

i=1
def atkien(x,y,z,i,nO,tol):
    while i < nO:
        p = x - (y-x)**2/(z-2*y+x)
        print(f'El valor de p en la iteracion {i} es {p}')
        if abs(p-x) < tol:
            print(f'La raiz es {p}')
            break
        x = p
        i+=1
    return print(f'Usando el metodo de Atkien. El valor de p es {p} y el numero de iteraciones es {i}'),p

atkien(first_three_values[0],first_three_values[1], first_three_values[2],i,nO,tol)