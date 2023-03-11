s = input().split('.')

for i in s:
    if int(i) < 0 or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')