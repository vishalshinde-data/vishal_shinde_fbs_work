# WAP to print armstrong number within a given range.

n = int(input('enter armstrong number:'))
for num in range(1, n+1):

    temp = num
    sum = 0
    count = 0
while(temp > 0):
    count += 1
    temp = temp // 10   
temp = num
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)

