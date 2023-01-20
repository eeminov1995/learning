# Наименьшее из четырёх чисел
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
if num_1 < num_2:
    ab = num_1
else: 
    ab = num_2
if num_3 < num_4:
    cd = num_3
else:
    cd = num_4
if ab < cd:
    print(ab)
else:
    print(cd)