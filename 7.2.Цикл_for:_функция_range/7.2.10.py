# Последовательность чисел 4

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 15 == 0:
        print(i)