#check palindrome number.

def palindrome():
    n = int(input('enter palindrome number:'))
    temp = n
    rev = 0

    while(n > 0):
        d = n % 10
        n = n // 10
        rev = rev * 10 + d

    if(rev == temp):
        print('number is palindrome')
    else: 
        print('number is not palindrome')  
palindrome()            


