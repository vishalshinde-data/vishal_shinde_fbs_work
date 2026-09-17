li = [40, 50, 30, 20, 10, 60]

max = li[0]
sec_max = 0
for ind in range(1, len(li)):
    if(li[ind] > max ):
        sec_max = max
        max = li[ind]
    elif(li[ind] > max):
        sec_max = max    

print('max:', max)
print('Sec_max:', sec_max)