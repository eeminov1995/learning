# YES or NO вот в чем вопрос

n = int(input())

if n % 2 != 0:
    print("YES")
elif n % 2 == 0 and 1 < n < 6:
    print("NO")
elif n % 2 == 0 and 5 < n < 21:
    print("YES")
elif n % 2 == 0 and 20 < n:
    print("NO")