# Тригонометрическое выражение

from math import *

x = float(input())
r = (x * pi) / 180
res = sin(r) + cos(r) + tan(r) ** 2

print(res)