n = int(input())
l_digit = n % 10
counter = 0
while n > 0:
    n_l_digit = n % 10
    n //= 10
    if l_digit != n_l_digit:
        counter += 1
if counter > 0:
    print('NO')
else:
    print('YES')
