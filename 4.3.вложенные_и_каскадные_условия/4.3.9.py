# Цветовой микшер 🌶️
color1 = input()
color2 = input()
if color1 == "красный" or color1 == "синий" or color1 == "желтый" and color2 == "красный" or color2 == "синий" or color2 == "желтый":
    color1 + color2
    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        print("фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        print("оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        print("зеленый")
    elif color1 == "синий" and color2 == "синий":
        print("синий")
    elif color1 == "красный" and color2 == "красный":
        print("красный")
    elif color1 == "желтый" and color2 == "желтый":
        print("желтый")
    else:
        print("ошибка цвета")
elif color1 != "синий" or color1 != "красный" or color1 != "желытй" and color2 != "синий" or color2 != "красный" or color2 != "желытй":
    print("ошибка цвета")
