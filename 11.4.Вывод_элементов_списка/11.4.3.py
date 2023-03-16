n = int(input())
l = []

for _ in range(n):
    a = int(input())
    l.append(a)
    print(a)
    
print()

for i in l:
    b = i ** 2 + 2 * i + 1
    print(b)