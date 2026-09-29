#Write a program to find sum of digit of number.


def number(num):

    d1 = num % 10
    num = num // 10

    d2 = num % 10
    num = num // 10
    
    d3 = num % 10
    num = num // 10

    sum = (d1 + d2 + d3)

    num = int(input("Enter the number:"))

    number(num)    
    
    


