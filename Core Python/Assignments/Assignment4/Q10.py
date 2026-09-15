#WAP to check if given number is perfect number.

num = int(input('Enter the number:'))
sum = 0

for i in range(1, num):
    if(num % i == 0):
        sum = sum+i
if(sum == num):
    print('The number is perfect number')
else:
    print('The number is not perfect number')    
