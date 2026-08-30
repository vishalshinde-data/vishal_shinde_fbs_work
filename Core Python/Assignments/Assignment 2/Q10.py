# Write a program to reverse three digit number.

num = int(input('Enter the three digit number:'))

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10

reverse = a * 100 + b * 10 + c

print('Reverse number:', reverse)

