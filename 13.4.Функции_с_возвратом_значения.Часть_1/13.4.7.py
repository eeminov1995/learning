# объявление функции
def get_days(month):
    x31 = [1, 3, 5, 7, 8, 10, 12]
    x30 = [4, 6, 9, 11]
    x28 = 2
    if month in x31:
        return 31
    elif month in x30:
        return 30
    else:
        return 28

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))