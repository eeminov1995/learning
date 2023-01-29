num = int(input())
i = 0
while num != 0:
    if num >= 25:
        num -= 25
        i += 1
    elif num >= 10:
        num -= 10
        i += 1
    elif num >= 5:
        num -= 5
        i += 1
    elif num >= 1:
        num -= 1
        i += 1
print(i)