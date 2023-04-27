# объявление функции
def get_month(language, number):
    if language == 'en':
        return ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'][number - 1]
    elif language == 'ru':
        return ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'][number - 1]
        

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))