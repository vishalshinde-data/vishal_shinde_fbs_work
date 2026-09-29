# Sum of all prime numbers between 1 to n.

def prime(n):
    total = 0

    for i in range(2, n+1):
        count = 0
        for j in range(1, i+1):
            if(i % j == 0):
                 count += 1
        if(count == 2):
            total += i         
    return total      
    
n = int(input("Enter prime number:"))
res = prime(n)
print("Addition of prime number:", res)
        
        