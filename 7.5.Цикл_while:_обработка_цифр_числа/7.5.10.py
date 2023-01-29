num = int(input())
flag = 'YES'           
a = num % 10          

while num:            
    if a > num % 10:  
        flag = 'NO'    
    else:             
        a = num % 10  
    num //= 10        
print(flag)