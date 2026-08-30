#Write a program to calculate area of an equilateral triangle.

import math
a = int(input('Enter side of triangle:'))

area = (math.sqrt(3) / 4) * a * a

print('Area of equilateral triangle:',area)