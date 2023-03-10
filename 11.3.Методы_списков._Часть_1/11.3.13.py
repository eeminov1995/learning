n = int(input())
sp = []

for _ in range(n):
    sp.append(input())
    
index = int(input())    
res = ""

for i in sp:
    if len(i) >= index:
        res += i[index - 1]
    
print(res)