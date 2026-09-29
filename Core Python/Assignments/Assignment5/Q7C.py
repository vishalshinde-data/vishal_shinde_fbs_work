#Geometric series from 1 to n , common ratio = 2

n = int(input("Enter the number:"))

term = 1
sum = 0
for i in range(n):
    sum = sum + term
    term = term * 2
print("sum=", sum)    