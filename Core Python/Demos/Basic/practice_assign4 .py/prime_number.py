#########################################
num = int(input("Enter the prime number:"))

if(num > 1):
    for i in range(2, num):
        if(num % i == 0):
            print("Number is not prime number")
            break
    else:
        print("Number is prime number")    
else:
    print("Not a prime number")


##########################################
num = int(input("Enter the number:"))

for i in range(2, num):
    if(num % i == 0):
        print("not prime number")
        break
else:
    print("prime number")        


#########################################Addition
num = int(input("enter the number:"))

for i in range(2, num+1):
    for j in range(2, i ):
        if(i % j == 0):
            break
    else:        
        print(i,end = ' ')


