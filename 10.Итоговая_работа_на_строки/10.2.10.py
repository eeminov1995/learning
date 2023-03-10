s = input()

if s.count("f") == 1:
    print(-1)
elif s.count("f") == 0:
    print(-2)
else:
    s = s.replace("f", "k" , 1)
    print(s.find("f"))