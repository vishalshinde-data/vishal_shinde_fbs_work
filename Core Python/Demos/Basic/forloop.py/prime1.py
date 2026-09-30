#WAP to print prime numbers between 1 to n (like 1 to 100)

n = int(input('enter value of n:'))
for i in range(2, n+1):
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        print(i, end = ' ')    

