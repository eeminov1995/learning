s = input()
sim = 0

for i in range(len(s)):
    if s[i] != s[i].upper():
        sim += 1     
        
print(sim) 