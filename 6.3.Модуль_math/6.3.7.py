# Квадратное уравнение 🌶️🌶️from math import *

a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Нет корней")