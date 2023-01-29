num = int(input())
min_1 = 10
max_1 = -1
while num != 0:
    last_digit = num % 10
    if last_digit > max_1:
        max_1 = last_digit
    if last_digit < min_1:
        min_1 = last_digit
    num //= 10
print(f'''Максимальная цифра равна {max_1}
Минимальная цифра равна {min_1}''')