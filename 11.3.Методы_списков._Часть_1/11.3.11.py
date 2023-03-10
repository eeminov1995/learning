n, a = int(input()), int(input())
sp = []

for _ in range(n - 1):
    b = int(input())
    sp.append(a + b)
    a = b
    
print(sp)