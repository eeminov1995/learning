s = []

for _ in range(int(input())):
    n = input()
    if n in s:
        continue
    else:
        s.append(n)
        
print(*s, sep='\n')