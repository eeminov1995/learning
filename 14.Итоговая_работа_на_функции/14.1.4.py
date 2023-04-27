# объявление функции
def draw_triangle():
    x = "*"
    for i in range(8):
        print(" " * (8 - 1 - i) + "*" * (1 + i * 2))
            
# основная программа
draw_triangle()  # вызов функции