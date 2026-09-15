#check strong number.

def strong(n):   
    
    temp = n
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1, d+1):
             fact = fact * i
        sum = sum + fact

    if(sum == n):
        print(f'{n} is strong.')
    else:
        print(f'{n} is not strong.')  
num = int(input('enter number:'))                  
strong(num)