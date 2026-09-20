# Sum of all prime numbers between 1 to n.

def prime(n):
    count = 0
    for i in range(1, n+1):
        if(n % i == 0):
            count += 1
    if(count == 2):
        return True
    else:
        return False
    

n = int(input("Enter prime number:"))
res = prime(n)
print("Addition of prime number:", res)
        
        