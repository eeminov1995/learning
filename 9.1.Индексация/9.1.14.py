s = input()
glasn = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
soglasn = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
counter_glasn = 0
counter_soglasn = 0

for i in range(len(s)):
    if s[i] in glasn:
        counter_glasn += 1
    if s[i] in soglasn:
        counter_soglasn += 1
print(f"Количество гласных букв равно {counter_glasn}", f"Количество согласных букв равно {counter_soglasn}", sep="\n")