li = [40, 50, 30, 20, 10, 60]

max = li[0]
smax = 0
for ind in range(1, len(li)):
    if(li[ind] > max):
        smax = max
        max = li[ind]
    elif(li[ind] > max):
        smax = max
print('Maximum number:', max)
print('Sec_maximum number:', smax)            
