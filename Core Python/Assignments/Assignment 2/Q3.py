#Convert distant given in feet and inches into meter and centimeter.

feet = int(input('Enter distance in feet:'))
inches = int(input('Enter distance in inches'))

meter = feet * 0.3048
centimeter = inches * 2.54

print('Distance in meter:', meter)
print('Distance in centimeter:', centimeter)