#write a program to check if given 3 digit number is palindrome or not.

num = int(input('Enter the palindrome number:'))
temp = num
rev = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev = rev * 10 + d

if(rev == num):
    print('The number is palindrome')
else:
    print('The number is not palindrome')    