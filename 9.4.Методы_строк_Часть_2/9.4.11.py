n = input()
count = 0  

for i in range(10):
    count += n.count(str(i))
    
print(count)