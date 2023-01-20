# Цвета колеса рулетки
pocket = int(input())
if 0 < pocket < 11:
    if pocket % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 10 < pocket < 19:
    if pocket % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 18 < pocket < 29:
    if pocket % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 28 < pocket < 37:
    if pocket % 2 == 0:
        print("красный")
    else:
        print("черный")
elif pocket == 0:
    print("зеленый")
else:
    print("ошибка ввода")