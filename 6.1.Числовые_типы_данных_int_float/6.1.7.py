# Dog age
n = int(input())
age = 0
if n < 3:
    age = n * 10.5
    print(age)
elif n > 2:
    age = (n - 2) * 4 + 21
    print(age)