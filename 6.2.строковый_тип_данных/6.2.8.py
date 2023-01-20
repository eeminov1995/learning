# Три города
city_1 = input()
city_2 = input()
city_3 = input()
x = len(city_1)
y = len(city_2)
z = len(city_3)
if min(x, y, z) == len(city_1):
    print(city_1)
elif min(x, y, z) == len(city_2):
    print(city_2)
elif min(x, y, z) == len(city_3):
    print(city_3)
if max(x, y, z) == len(city_1):
    print(city_1)
elif max(x, y, z) == len(city_2):
    print(city_2)
elif max(x, y, z) == len(city_3):
    print(city_3)  