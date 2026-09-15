#check perfect number.

def perfect(n):
    sum = 0

    for i in range(1, n):
        if(n % i == 0):
            sum = sum+i
    if(sum == n):
        print('perfect number')
    else:
        print('Not perfect number')     
n = int(input('enter the perfect number:'))               
perfect(n)        