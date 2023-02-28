s = input()               

a = s.find('h')            
b = s.rfind('h')          
c = s[a:b + 1] 

print(s.replace(c, ''))