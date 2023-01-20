# Евклидово расстояние

from math import *

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

res = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(res)