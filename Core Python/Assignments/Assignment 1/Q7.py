# Program to find the roots of a quadratic equation.
import math

a = int(input('enter a:'))
b = int(input('enter b:'))
c = int(input('enter c:'))

d = b * b - 4 * a * c

if(d > 0):
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b + math.sqrt(d)) / (2 * a)

    print('Root 1:', root1)
    print('Root 2:', root2)

elif d == 0:
    root = -b / (2 * a)
    print('both roots are:', root)

else:
    print('Roots are complex')        