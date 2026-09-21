#WAP to calculate sum of all programs.
li = [[10, 20], [30, 40], [50, 60]]

sum = 0
for i in li:
    for j in i:
        sum += j
print(sum)        