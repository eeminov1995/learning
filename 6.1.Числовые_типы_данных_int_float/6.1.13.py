# Сортировка трёх 🌶️
n1 = int(input())
n2 = int(input())
n3 = int(input())
n_min = min(n1, n2, n3)
n_max = max(n1, n2, n3)
n_middle = (n1 + n2 + n3) - n_min - n_max
print(n_max, n_middle, n_min, sep="\n")