#Write a program to enter P,T,R and calculate simple interest

p = int(input('Enter principle:'))
t = int(input('Enter time;'))
r = int(input('Enter rate of interest:'))

si =(p * t * r) / 100
print('simple interest:', si)

