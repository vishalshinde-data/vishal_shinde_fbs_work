n = 4
for i in range(1,5):
    for j in range(1,n-i):
        print(' ', end = ' ')
    for j in range(1, 6-i):
        print(j, end = ' ')
     
    print()        