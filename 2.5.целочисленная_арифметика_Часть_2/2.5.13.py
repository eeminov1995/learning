# Трехзначное число
# put your python code here
n = int(input())
a = n % 10
b = (n % 100) // 10
c = n // 100
s = (a + b + c)
p = (a * b * c)
print("Сумма цифр = " + str(s))
print("Произведение цифр = " + str(p))
