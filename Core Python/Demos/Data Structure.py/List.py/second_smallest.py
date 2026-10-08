li = [20, 40, 10, 50, 70, 60, 30]
min = li[0]
s_min = 0
for i in range(1, len(li)):
    if(li[i] < min):
        s_min = min
        min = li[i]
    elif(li[i] < s_min):
        s_min == li[i]

print("Minimum number is:", min)
print("Second minimum number is:", s_min)            