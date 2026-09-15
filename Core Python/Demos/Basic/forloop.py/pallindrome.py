#WAP to check given number is pallindrome or not.

num = int(input('enter the number:'))
temp = num
rev_num = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d

if(rev_num == num):
    print('The number is palindrome')
else:
    print('The number is not palindrome.')


