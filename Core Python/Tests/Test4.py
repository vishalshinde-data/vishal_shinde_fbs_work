#Q1.
def factors(n):
    for i in range(1, n+1):
        if (n % i == 0):
            print(i, end = " ")
factors(15) 

#Q2.
def factorial(n):
    if(n ==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial=", factorial(num))    


#Q3.

for i in range(23):
    print("*", end = " ")
print()

for i in range(11):
    print(" " * (22-i) + "*")

for i in range(11):
    print(" " * (12) + "*")

for i in range(23):
    print("*", end = " ")