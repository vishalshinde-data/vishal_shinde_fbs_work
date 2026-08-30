# divisible by 5.
num = int(input('enter the number:'))

if(num % 5 == 0):
    print('number is divisible by 5')
else:
    print('number is not divisible by 5')    

#num is divisible by 3 and 5.

num = int(input('enter the number:'))

if(num % 5 == 0  and num % 3 == 0):
    print('number is divisible by both')
else:
    print('number is not divisible by both')    