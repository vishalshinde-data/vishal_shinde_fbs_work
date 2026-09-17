#Method1
lis = [30, 40, 80, 90, 10, 20, 60]
largest  = 0
for i in lis:
    if i > largest:
        largest = i   
print(largest)    

#Method2: used in class
li = [40, 50, 30, 20, 10, 60]

max = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max ):
        max = li[ind]

print('Maximum number:', max)