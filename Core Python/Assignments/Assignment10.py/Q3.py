#Write a program to find the second largest element in the list.

li = [20, 30, 10, 50, 40, 70, 80, 60]

max = li[0]
s_max = 0

for i in range(1, len(li)):
    if(li[i] > max):
        s_max = max
        max = li[i]
    elif(li[i] > max):
        s_max = max  

print("Maximum number:", max)
print("Second maximum number:", s_max)