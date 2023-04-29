# объявление функции
n = int(input())

def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return 1000 + (quantity * 120 - 120)
    

# считываем данные


# вызываем функцию
print(get_shipping_cost(n))