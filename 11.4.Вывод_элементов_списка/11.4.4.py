n = int(input())
l = []

for _ in range(n):
    num = int(input())
    l.append(num)
    
for i in l:
    if i != min(l) and i != max(l):
        print(i)