# Write a program to swap two numbers without using third variable.

a = int(input('enter first number:'))
b = int(input('enter second number:'))

a,b = b,a

print('After swapping:')
print('a:',a)
print('b:',b)