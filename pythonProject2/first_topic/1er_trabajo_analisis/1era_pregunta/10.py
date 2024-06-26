import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def f(a,b,c):
    x1 = (-2*c)/(b+math.sqrt(b**2-4*a*c))
    x2 = (-2*c)/(b-math.sqrt(b**2-4*a*c))
    return x1,x2,print(f'x1 = {x1} y x2 = {x2}')

f(1,1,-6)

