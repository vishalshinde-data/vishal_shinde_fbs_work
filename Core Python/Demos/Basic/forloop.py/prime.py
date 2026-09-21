num = int(input("Enter the number:"))

for i in range(1, num):
    if(num % i == 0):
        print(f"{num} is not prime number.")
        break
else:
    print(f" {num} is prime number.")        


