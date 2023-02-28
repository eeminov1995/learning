n = int(input())
s = input()
sim = 26

for i in range(len(s)):
    w = ord(s[i]) - n
    if w < 97:
        w += sim
    print(chr(w), end="")
