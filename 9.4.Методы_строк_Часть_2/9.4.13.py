s = input()              

c = 0                    
a = ''   

for i in s:            
    if s.count(i) >= c:  
        c = s.count(i)   
        a = i          
        
print(a)