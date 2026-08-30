#sum of odd numbers.
sum = 0
for i in range(1,101):
    if(i % 2 != 0):
        sum = sum + i
print('sum of odd number:',sum)   

#sum of even numbers.

sum = 0
for i in range(1,101):
    if(i % 2 == 0):
        sum = sum + i
print('sum of even number:',sum)        