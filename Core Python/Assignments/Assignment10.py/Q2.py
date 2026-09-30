#Write a program to find maximum and minimum element in a list.

li = [20, 40, 50, 10, 60, 80, 70]

max = li[0]
min = li[0]
for ind in range(1, len(li)):
    if(li[ind] > max):
        max = li[ind]
    elif(li[ind] < min):
        min = li[ind]    
print("Maximum number:", max)
print("Minimum number:", min)        