#check palindrome number.

def palindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        d = n % 10
        n = n // 10
        rev = rev * 10 + d
    if(rev == temp):
        print('Number is palindrome')
    else:
        print('Number is not palindrome')
num = int(input('Enter the palindrome number:'))
palindrome(num)        