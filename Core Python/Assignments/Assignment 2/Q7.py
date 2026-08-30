#find the sum of three digit.

num = int(input('Enter the number'))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3

print(f'The sum of {d1},{d2} and {d3} is {sum}')