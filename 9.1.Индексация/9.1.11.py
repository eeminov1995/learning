s = input()
flag = "Цифр нет"

for i in range(len(s)):
    if s[i] in "0123456789":
        flag = "Цифра"
        
print(flag)