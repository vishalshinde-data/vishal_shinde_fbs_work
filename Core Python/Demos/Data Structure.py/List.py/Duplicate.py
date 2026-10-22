#Find the duplicate value

a = [10, 30, 20, 80, 10, 60, 20]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i] == a[j]):
            print(a[i])


li = [10, 30, 20, 80, 10, 80, 60, 20]
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if(li[i] == li[j]):
            print(li[i])


