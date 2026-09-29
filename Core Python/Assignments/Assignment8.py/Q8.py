#Write a program to find reverse of a number.

def reverse(n):

    rev = 0
    while(n > 0):
        digit = n % 10
        n = n // 10
        rev = rev * 10 + digit
    print("reverse number is", rev)

n = int(input("enter the number:"))
reverse(n)   
