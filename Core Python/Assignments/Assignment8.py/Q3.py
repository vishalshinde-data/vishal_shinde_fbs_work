#Write a program to find sum of following series using function
##A: 1 + 2 + 3 + 4 +....+n
def sum(n):
    count = 0
    for i in range(1, n+1):
        count += i
    return count  
n = int(input("Enter the number:"))  
res =  sum(n)     
print("addition is", res)        



##B:
