# Средние значения

from math import *

a = float(input())
b = float(input())

res1 = (a + b) / 2
res2 = sqrt(a * b)
res3 = 2 * a * b / (a + b)
res4 = sqrt((a ** 2 + b ** 2) / 2)

print(res1, res2, res3, res4, sep="\n")
