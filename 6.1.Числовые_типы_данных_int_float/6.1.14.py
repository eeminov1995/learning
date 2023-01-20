# Интересное число
num = int(input())
n1 = num // 100
n2 = num // 10 % 10
n3 = num % 10
x_min = min(n1, n2, n3)
x_max = max(n1, n2, n3)
x_middle = (n1 + n2 +n3) - x_max - x_min
if x_middle == x_max - x_min:
    print("Число интересное")
else:
    print("Число неинтересное")