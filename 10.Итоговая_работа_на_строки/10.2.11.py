s = input()
a = s.find("h")
b = s.rfind("h")

print(s[:a] + s[b:a:-1] + s[b:])
