s = input().split()
counter = 0

for i in s:
    n = s.count(i) - 1
    counter += n
    s = s[1:]
    
print(counter)