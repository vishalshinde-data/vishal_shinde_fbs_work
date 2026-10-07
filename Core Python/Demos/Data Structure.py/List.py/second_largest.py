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

max = li[0]
smax = 0
for ind in range(1, len(li)):
    if(li[ind] > max):
        smax = max
        max = li[ind]
    elif(li[ind] > smax):
        smax = li[ind]
print("Maximum number:", max)
print("Second Minimum number:", smax)            




