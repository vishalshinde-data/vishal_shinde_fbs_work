#check prime number 

def prime():
    n = int(input('enter the number:'))
    count = 0

    for i in range(1, n+1 ):
        if(n % i == 0):
            count +=1        #count = count+1
    if(count == 2):
        print('prime number')
    else:
        print('Not prime number')    
prime()        