#Write a program to input all sides of a triangle and check whether triangle is valid or not.


x = int(input('enter first side:'))
y = int(input('enter second side:'))
z = int(input('enter third side:'))

if(x+y>z and y+z>x and x+z>y):
    print('Triangle is valid.')
else:
    print('Triangle is invalid.')    
