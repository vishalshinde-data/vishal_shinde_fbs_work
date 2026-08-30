#find the largest of 3 numbers using nested if.

a = int(input('enter first number:'))
b = int(input('enter second number:'))
c = int(input('enter third number:'))

if(a > b):
    if(a > c):
        print('largest:',a)
    else:
        print('largest:',c)

else:
    if(b > c):
        print('largest:',b)
    else:
        print('largest:',c)    