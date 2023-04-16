# объявление функции
def number_of_factors(num):
    sp = []

    for i in range(1, num + 1):
        if n % i == 0:
            sp.append(i)
    return len(sp)


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))