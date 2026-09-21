#find the smallest number.

numbers = [10, 23, 3, 1, 76, 84, 74]

smallest = numbers[0]

for i in numbers:
    if(i < smallest):
        smallest =i
        
print('smallest number:', smallest)        

#find the largest number.

numbers = [10, 23, 3, 1, 76, 84, 74]

largest = numbers[0]

for i in numbers:
    if(i > largest):
        largest = i

print('largest number:', largest)        