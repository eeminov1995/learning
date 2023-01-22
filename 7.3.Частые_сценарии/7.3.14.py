# Only even numbers 🌶️

Flag = True
for i in range(10):
    n = int(input())
    if n % 2 != 0:
        Flag = False
if Flag:
    print("YES")
else:
    print("NO")
