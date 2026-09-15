palindrome = lambda n : str(n) == str (n)[::-1]

num = int(input('enter number:'))

if(palindrome(num)):
    print('palindrome number')
else:
    print('not palindrome number')    