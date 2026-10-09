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


# you can also write this
def palindrome(n):
    temp = n
    rev = 0
    while(temp> 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    if(rev == n):
        print("the number is palindrome.")
    else:
        print("the number is not palindrome.")        

num = int(input("enter the number:"))
palindrome(num)        