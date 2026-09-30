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

#method 2
li = [10, 30, 3 , 20 ,50 ,60]
min = li[0]
for i in range(1, len(li)):
    if(li[i] < min):
        min = li[i]
print("smallest number:", min)        