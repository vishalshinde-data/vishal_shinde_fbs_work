#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input('enter first side:'))
b = int(input('enter second side:'))
c = int(input('enter third side:'))

if(a == b and b == c):
    print('equilateral triangle')
elif(a == b and b == c and c == a):
    print('isosceles triangle')
else:
    print('scalene  triangle')        