s = input()
c1 = 0
c2 = 0
for i in range(0, len(s)):
    if "+" in s[i]:
        c1 += 1
    if "*" in s[i]:
        c2 += 1
    
print(f"Символ + встречается {c1} раз", f"Символ * встречается {c2} раз", sep="\n")