s = input()
l = len(s)
x = l // 2 + l % 2
res = s[x:] + s[:x]

print(res)