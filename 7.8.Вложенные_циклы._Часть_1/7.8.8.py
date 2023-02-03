n = int(input())
for i in range(1, n // 2  + 2):
    print('*' * i, end='')
    print()
for i in range(n // 2, 0, -1):
    print('*' * i, end='')
    print()