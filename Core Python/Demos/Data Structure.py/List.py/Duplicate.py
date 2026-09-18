#Find the duplicate value

a = [10, 30, 20, 80, 10, 60, 20]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(a[i])
