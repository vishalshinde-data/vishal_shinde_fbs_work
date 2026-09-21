#sum of odd numbers.
num = int(input("Enter the odd number:"))
sum = 0
for i in range(1,num):
    if(i % 2 != 0):
        sum = sum + i
print('sum of odd number:',sum)   

#sum of even numbers.
num = int(input("Enter the even number:"))
sum = 0
for i in range(1,num):
    if(i % 2 == 0):
        sum = sum + i
print('sum of even number:',sum)        