# Возрастная группа
age = int(input())
if age <= 13:
    print("детство")
if 13 < age < 25:
    print("молодость")
if 24 < age < 60:
    print("зрелость")
if age >= 60:
    print("старость")