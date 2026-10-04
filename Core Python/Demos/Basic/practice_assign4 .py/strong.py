num = int(input("Enter the number:"))
temp = num
total = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    fact = 1

    for i in range(1, d+1):
        fact = fact * i
    total= total + fact

if(num == total):
    print("number is strong")
else:
    print("number is not strong")            

