#Method1
lis = [30, 40, 80, 90, 10, 20, 60]
largest  = 0
for i in lis:
    if i > largest:
        largest = i   
print(largest)    

#Method2: used in class
li = [20, 30, 60, 10, 70, 90, 80]
max = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]
print("Maximum Number :", max)  

