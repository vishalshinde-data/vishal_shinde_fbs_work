#1
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end = ' ')
    print()

#2.
for i in range(1, 6):
    for j in range(1, 7-i):
        print('*', end = ' ')
    print()  

#3. increasing number pattern.
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()     

#4. decreasing number pattern.
for i in range(1,6):
    for i in range(1, 7-i):
        print(i, end = ' ')
    print()             