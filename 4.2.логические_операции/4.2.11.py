# Красивое число
x = int(input())
if (999 < x < 10000) and (x % 7 == 0 or x % 17 == 0):
    print("YES")
else:
    print("NO")