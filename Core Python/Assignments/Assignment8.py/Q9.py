#Write a program to check if entered number is pelindrome or not.

def palindrome(n):
    total = n
    rev_num = 0
    while(n > 0):
        digit = n % 10
        n = n // 10
        rev_num = rev_num * 10 + digit
    if(rev_num == total):
        print("number is palindrome number")
    else:
        print("number is not palindrome number")    
n = int(input("enter the number:"))     
palindrome(n)       


