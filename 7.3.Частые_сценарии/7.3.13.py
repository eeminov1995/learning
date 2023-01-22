# Наибольшие числа 🌶️🌶️

n = int(input())
max1, max2 = -1, -1
for i in range(n):
    x = int(input())
    if x > max1:
        max1, max2 = x, max1
    elif x > max2:
        max2 = x
print(max1, max2, sep="\n")
