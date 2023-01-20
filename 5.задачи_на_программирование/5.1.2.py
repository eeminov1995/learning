# Шахматная доска

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

s = (x1 + x2 + y1 + y2)

if s % 2 ==  0:
    print("YES")
else:
    print("NO")