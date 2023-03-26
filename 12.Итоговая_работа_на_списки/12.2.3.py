n = [int(i) for i in input().split()]
print(*n, sep='+', end='=')
print(sum(n))