# Правильный многоугольник

from math import *

n = int(input())
a = float(input())

S = (n * a ** 2) / (4 * tan(pi / n))

print(S)