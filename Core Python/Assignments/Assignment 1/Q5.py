#Write a program to enter P T R and calculate compound interst.

p = int(input('Ente principle amount:'))
r = int(input('Enter rate of intrest:'))
t = int(input('Enter time:'))

amount = p * (1 + r / 100) ** t
ci = amount - p

print('Compound intrest:',ci)
print('Amount:',amount)