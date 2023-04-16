a, b = input().split(), input().split()
print(*(int(a[i]) + int(b[i]) for i in range(len(a))))