#check whether a number is positive.if positive check whether it is even or odd.

num = int(input('enter the number:'))

if(num > 0):
    if( num % 2 == 0):
        print('positive even number')
    else:
        print('positive odd number')
else:
    print('number is not positive')            