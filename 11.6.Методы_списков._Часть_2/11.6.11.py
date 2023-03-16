n = input().split() 

for i in range(len(n)):
    n[i] = int(n[i])
    
n.sort()
print(*n)
n.sort(reverse = True)
print(*n)