# объявление функции
def get_factors(num):
    sp = []

    for i in range(1, num + 1):
        if num % i == 0:
            sp.append(i)
    return sp


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))