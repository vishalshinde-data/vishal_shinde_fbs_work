a = [20, 40, 10, 50, 70, 60, 30]
min = a[0]
smin = 0
for i in range(1, len(a)):
    if(a[i] < min):
        smin = min
        min = a[i]
    elif(a[i] < smin):
        smin = a[i]
print("Minimum number:", min)
print("Second Minimun number:", smin)            