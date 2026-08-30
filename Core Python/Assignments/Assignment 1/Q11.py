#Find the area of circumference of circle.
import math
r = int(input('Enter radius:'))

area = math.pi * r * r
circumference = 2 * math.pi * r

print('area of circle:', area)
print('circumference of circle:', circumference)