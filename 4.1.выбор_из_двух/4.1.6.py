# Соотношение
num = int(input())
num_1 = num // 1000
num_2 = num // 100 % 10
num_3 = num // 10 % 10
num_4 = num % 10 
if num_1 + num_4 == num_2 - num_3:
    print("ДА")
else:
    print("НЕТ")



