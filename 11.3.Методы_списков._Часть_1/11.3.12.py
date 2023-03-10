n = int(input())
b = []

for i in range(n):
    a = int(input())
    b.append(a)

del b[1::2]

print(b)