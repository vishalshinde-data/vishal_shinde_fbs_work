#Find even and odd numbers from list.

li = [10, 23, 22, 45, 67, 88, 98, 15, 56]
even = 0
odd = 0
for i in li:
    if(i % 2 == 0):
        print("even number:", i)
    else:
        print("odd number:", i) 

#Find separate even and odd numbers from list.
li = [10, 23, 22, 45, 67, 88, 98, 15, 56]
even = []
odd = []
for i in li:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)                    
print("Odd numbers:", odd)        