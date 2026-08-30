#for i in range(2, 21,2):
#for i in range(5, 51, 5):

# multiplication table
n = int(input('enter number:'))
for i in range(n, n * 10 + 1, n):
    print(i)    

#reverse multiplication table    
n = int(input('enter the number'))
for i in range(n * 10, n - 1, -n):
    print(i)    

