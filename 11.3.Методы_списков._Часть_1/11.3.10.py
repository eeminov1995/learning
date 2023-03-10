n = int(input())
sp = []

for i in range(1, n + 1):
    if n % i == 0:
        sp.append(i)

print(sp)