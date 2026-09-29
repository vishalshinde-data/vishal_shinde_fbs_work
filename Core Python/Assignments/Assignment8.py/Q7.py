#Write a program to find sum of digit of number.


def sum_digit(num):
    sum = 0
    while(num > 0):
        digit = num % 10
        num = num // 10
        sum = sum + digit
    return sum

num = int(input("enter thr number:"))
result = sum_digit(num) 
print("sum of digit:", result)   
    
