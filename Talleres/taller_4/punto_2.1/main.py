"""
@author: Andres Giraldo, Camilo Garcia, David Ramirez
"""
from euler import *
from matplotlib.pyplot import *


def f(a, y):
    return (-1 * a) * y  # Funcion y' = -αy


m = 100  # Valor final del intervalor
a0 = 0  # Valor inicial de α
y0 = 1  # Valor inicial de y
h = 0.1  # Cantidad para el paso
[u, v] = euler(f, a0, y0, h, m)

# Grafica
plot(u, v, "b")
title("Solución numerica método Euler")
xlabel("α")
ylabel("y")
show()
