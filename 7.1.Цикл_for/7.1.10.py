# put your python code here

m = float(input())
p = float(input())
n = int(input())

for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)