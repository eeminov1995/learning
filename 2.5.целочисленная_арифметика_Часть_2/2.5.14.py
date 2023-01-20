# Перестановка цифр
n = int(input())
a = n % 10
b = (n % 100) // 10
c = n // 100
print(str(c) + str(b) + str(a))
print(str(c) + str(a) + str(b))
print(str(b) + str(c) + str(a))
print(str(b) + str(a) + str(c))
print(str(a) + str(c) + str(b))
print(str(a) + str(b) + str(c))