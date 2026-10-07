#Odd numbers
a = [10, 75, 30, 53, 50, 60, 41, 80]
count = 0
for i in range(0, len(a)):
    if(a[i] % 2 != 0):
        count += 1
print("Odd number:", count)        
