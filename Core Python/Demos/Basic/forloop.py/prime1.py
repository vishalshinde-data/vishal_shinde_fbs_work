#WAP to print prime numbers between 1 to n (like 1 to 100)

n = int(input('enter value of n:'))
for num in range(2, n+1):
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end = ' ')    

#HM: WAP to print first n prime numbers.        