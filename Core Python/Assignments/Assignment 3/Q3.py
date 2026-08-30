#Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input('enter first triangle:'))
b = int(input('enter second triangle:'))
c = int(input('enter third  triangle:'))

if(a + b + c == 180):
    print('triangle is valid.')
else:
    print('triangle is not valid.')    