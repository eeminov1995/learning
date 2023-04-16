# объявление функции
def print_digit_sum(num):
    total = 0
    for i in str(num):
        total += int(i)
    print(total)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)