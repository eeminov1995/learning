n = int(input())
l = []

for _ in range(n):
    a = int(input())
    l.append(a)
    
for i in l:
    if i < 0:
        print(i)
        
for i in l:
    if i == 0:
        print(i)
        
for i in l:
    if i > 0:
        print(i)