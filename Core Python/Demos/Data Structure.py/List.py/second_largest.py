li = [20, 40, 10, 50, 70, 60, 30]
max = li[0]
s_max = 0
for ind in range(1, len(li)):
    if(li[ind] > max):
        s_max = max
        max = li[ind]
    elif(li[ind] > s_max):
        s_max = li[ind]
        
print("Maximum number is ", max)
print("Second maximum number is", s_max)



li = [20, 40, 10, 50, 70, 60, 30]
max = li[0]
s_max = 0

for i in range(1, len(li)):
    if(li[i] > max):
        s_max = max
        max = li[i]
    elif(li[i] > s_max): 
        s_max = li[i]

print("maximum number:", max)
print("second maximum number:", s_max)
