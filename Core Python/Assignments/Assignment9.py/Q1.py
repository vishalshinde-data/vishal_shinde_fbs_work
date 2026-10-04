#Write a program to find the sum of following series using recursive function:
#1. 1! + 2! +3! 4! +......+ n+
def show(num):
    if(num == 0):
        return 0 
    else:
        return num + show(num-1)
    
num = int(input("Enter the number:"))
res = show(num)
print(res)

#Fact
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

num = int(input("Enter the number:"))
res = fact(num)
print(res)   