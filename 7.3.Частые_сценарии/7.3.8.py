# Сумма чисел 2

n = int(input())
total = 0
for i in range(1, n + 1):
    if i ** 2 % 10 == 2:
        total += i
    elif i ** 2 % 10 == 5:
        total += i
    elif i ** 2 % 10 == 8:
        total += i
print(total)