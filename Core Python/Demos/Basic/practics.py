#Write a program to swap two numbers without using third variable.

x=10
y=20

print(f'Before swapping: x={x}, y={y}')

x,y = y,x

print(f'After swapping: x={x}, y={y}')


#Find the sum of three digit number.

num=967

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

sum=d1+d2+d3
print(f'The addition of {d1},{d2},{d3} is {sum}')