#Write a program to find print the following fibonacci series 

def fibonaci(num):
    a = 1
    b = 1
    for i in range(num):
        c = a + b
        print(a, end = ' ')
        a = b
        b = c

num = int(input("Enter the number:"))

fibonaci(num)    