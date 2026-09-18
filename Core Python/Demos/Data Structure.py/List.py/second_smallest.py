a = [20, 40, 10, 50, 70, 60, 30]
min = a[0]
smin = 0
for i in range(1, len(a)):
    if(a[i] < min):
        smin = min
        min = a[i]
    elif(a[i] < min):
        smin = min
print('Smallest number:', min)
print('Second smallest number:', smin)            